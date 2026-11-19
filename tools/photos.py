"""Prepare an apartment's photos for the site.

Usage (from the repo root):
    python3 -I tools/photos.py <id> <folder with the photos> <cards>

<folder> holds the photos in gallery order (sorted by file name: 01.jpg, 02.jpg, ...).
<cards> is the list of photos used on the apartment card, by position in that order,
for example 1,2,13,18,16 (3 to 5 photos, landscape framing works best).

Writes images/u/<id>/NN.webp (gallery, longest side up to 1400 px), tNN.webp (thumbnails),
images/g/<id>-N.jpg and .webp (cards, 760x570), baixar/<id>-fotos.zip (the gallery photos as JPG,
for the "Baixar fotos" button) and the sizes in tools/photos.json.
Photos smaller than 640 px are enlarged to 640 px so the gallery keeps its layout.

    python3 -I tools/photos.py --zip <id>
only rebuilds baixar/<id>-fotos.zip from the gallery already in images/u/<id>/.
"""
import glob, io, json, os, shutil, sys, zipfile
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def write_zip(pid, photos):
    """baixar/<id>-fotos.zip with the gallery photos as JPG (<id>-01.jpg, <id>-02.jpg ...), in gallery order."""
    d = os.path.join(ROOT, 'baixar')
    os.makedirs(d, exist_ok=True)
    tmp = os.path.join(d, f'{pid}-fotos.zip.tmp')
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_STORED) as z:
        for i, im in enumerate(photos, 1):
            buf = io.BytesIO()
            im.convert('RGB').save(buf, 'JPEG', quality=90, optimize=True, progressive=True)
            info = zipfile.ZipInfo(f'{pid}-{i:02d}.jpg', date_time=(2020, 1, 1, 0, 0, 0))
            z.writestr(info, buf.getvalue())
    os.replace(tmp, os.path.join(d, f'{pid}-fotos.zip'))


def main():
    if sys.argv[1] == '--zip':
        pid = sys.argv[2]
        files = sorted(glob.glob(os.path.join(ROOT, 'images', 'u', pid, '[0-9][0-9].webp')))
        if not files:
            sys.exit('Nenhuma foto em images/u/' + pid)
        write_zip(pid, [Image.open(f) for f in files])
        print(f'{pid}: {len(files)} fotos no zip')
        return
    pid, src, cards = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(',')]
    files = sorted(f for f in glob.glob(os.path.join(src, '*')) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')))
    if not files:
        sys.exit('Nenhuma foto encontrada em ' + src)
    out = os.path.join(ROOT, 'images', 'u', pid)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    sizes, imgs, fulls = [], [], []
    for i, f in enumerate(files, 1):
        im = ImageOps.exif_transpose(Image.open(f)).convert('RGB')
        if max(im.size) < 640:
            k = 640 / max(im.size)
            im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
        imgs.append(im)
        full = im.copy(); full.thumbnail((1400, 1400), Image.LANCZOS)
        full.save(os.path.join(out, f'{i:02d}.webp'), quality=80, method=6)
        th = im.copy(); th.thumbnail((220, 220), Image.LANCZOS)
        th.save(os.path.join(out, f't{i:02d}.webp'), quality=72, method=6)
        sizes.append(list(full.size))
        fulls.append(full)
    write_zip(pid, fulls)
    for old in glob.glob(os.path.join(ROOT, 'images', 'g', pid + '-*')):
        os.remove(old)
    for n, c in enumerate(cards, 1):
        card = ImageOps.fit(imgs[c - 1], (760, 570), Image.LANCZOS, centering=(0.5, 0.55))
        card.save(os.path.join(ROOT, 'images', 'g', f'{pid}-{n}.jpg'), quality=78, optimize=True, progressive=True)
        card.save(os.path.join(ROOT, 'images', 'g', f'{pid}-{n}.webp'), quality=76, method=6)
    pj = os.path.join(ROOT, 'tools', 'photos.json')
    data = json.load(open(pj)) if os.path.exists(pj) else {}
    data[pid] = sizes
    json.dump(data, open(pj, 'w'), indent=1)
    print(f'{pid}: {len(files)} fotos na galeria, {len(cards)} no cartão')


if __name__ == '__main__':
    main()
