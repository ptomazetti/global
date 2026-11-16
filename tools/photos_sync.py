"""Keep each apartment's photos in step with its photo folder on Google Drive.

Called by tools/sync_status.py when it gets the Drive listing (see tools/AUTOMACAO.md).
For every apartment with a "fotos" folder in tools/drive_folders.json:
- the photos in the listing are put in folder order (by the number at the start of the
  file name: 1.jpg, 2.jpg ... 10.jpg, then other names alphabetically);
- if that list (file id and modified time) is the same as in tools/photos_src.json, nothing happens;
- otherwise the photos are downloaded, exact duplicates dropped, and the gallery and card
  photos are rebuilt with tools/photos.py:
    gallery = sharp photos (longest side 1200 px or more) in folder order, then the small ones;
    cards (the photos on the apartment card and in the description PDF) = the first 5 of the gallery.
A folder with no photo in the listing is left alone, so a failed Drive search never empties a gallery.

Returns the IDs whose photos changed; tools/sync_status.py prints a FOTOS line for them.
"""
import glob, hashlib, json, os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'tools', 'photos_src.json')
SHARP = 1200   # Drive gives 1600 px for a phone photo; smaller means the file in the folder is small


def order_key(f):
    m = re.match(r'\s*(\d+)', f.get('title') or f.get('name') or '')
    return (0, int(m.group(1)), f.get('title', '')) if m else (1, 0, f.get('title', ''))


def listing(files, folder):
    imgs = [f for f in files if f.get('parentId') == folder and str(f.get('mimeType', '')).startswith('image/')]
    return sorted(imgs, key=order_key)


def download(file_id, dest):
    url = f'https://drive.google.com/thumbnail?id={file_id}&sz=w1600'
    r = subprocess.run(['curl', '-sSLf', '--retry', '2', '-o', dest, url], capture_output=True)
    return r.returncode == 0 and os.path.getsize(dest) > 1000


def rebuild(pid, imgs):
    from PIL import Image
    work = tempfile.mkdtemp(prefix='fotos-')
    try:
        got, seen = [], set()
        for f in imgs:
            dest = os.path.join(work, f['id'] + '.jpg')
            if not download(f['id'], dest):
                print('FOTO_FALHOU', pid, f.get('title', f['id']))
                return False      # keep the site as it is; the next run tries again
            h = hashlib.sha1(open(dest, 'rb').read()).hexdigest()
            if h in seen:
                continue           # same photo twice in the folder
            seen.add(h)
            with Image.open(dest) as im:
                got.append((dest, max(im.size) >= SHARP))
        ordered = [d for d, sharp in got if sharp] + [d for d, sharp in got if not sharp]
        if not ordered:
            return False
        src = os.path.join(work, 'ordem'); os.makedirs(src)
        for i, d in enumerate(ordered, 1):
            shutil.copy(d, os.path.join(src, f'{i:02d}.jpg'))
        cards = ','.join(str(i) for i in range(1, min(5, len(ordered)) + 1))
        subprocess.run([sys.executable, '-I', os.path.join(ROOT, 'tools', 'photos.py'), pid, src, cards],
                       cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
        return True
    finally:
        shutil.rmtree(work, ignore_errors=True)


def sync(files, ids, folders):
    state = json.load(open(SRC, encoding='utf-8')) if os.path.exists(SRC) else {}
    changed = []
    for pid in ids:
        folder = folders.get(pid, {}).get('fotos')
        if not folder:
            continue
        imgs = listing(files, folder)
        if not imgs:
            continue
        sig = [[f['id'], f.get('modifiedTime', '')] for f in imgs]
        if state.get(pid) == sig:
            continue
        if rebuild(pid, imgs):
            state[pid] = sig
            changed.append(pid)
    if changed:
        json.dump(state, open(SRC, 'w', encoding='utf-8'), indent=1)
    return changed
