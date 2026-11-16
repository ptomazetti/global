"""Apply apartment availability, prices and Drive links, then rebuild the site.

Usage (from the repo root):
    python3 -I tools/sync_status.py '<json>' "fonte da mudança" [drive.json]

<json> maps each ID to either a status string, or an object with any of
"status", "rent", "condo", "iptu". Prices accept 3490, "3.490,00" or "R$ 3.490".
    {"red-1401": {"status": "Alugado"}, "vida-plena-c65": {"status": "Disponível", "rent": "2.790,00", "condo": "406,42", "iptu": "61,84"}}
IDs that are not in the list P of tools/build.py are skipped and listed on a FORA_DO_SITE line.

[drive.json] is optional: a file with the Google Drive listing of the folders in
tools/drive_folders.json (any JSON that contains the file objects with "id", "parentId",
"createdTime" and "mimeType", for example the search results saved as they came).
For each apartment it picks the video and the description PDF:
- a file added to the folder after the last check wins (the most recently added one);
- otherwise the current file stays while it is still in the folder;
- if the current file is gone, the most recently added file left in the folder is used.
A video folder with no files in the listing is left alone (the link is never blanked).
A description folder with no PDF (when the listing has PDFs from other folders) is marked
"gerado": tools/build.py then makes the description PDF itself (descricao/<id>.pdf).

- Writes tools/status.json ("units", "prices", "media").
- If anything changed, runs tools/build.py. Status or price changes also update ATUALIZADO
  (the "lista atualizada em" date) in tools/build.py to today's date in São Paulo.
- The last line printed is CHANGED (status or price changed), MEDIA (only video or
  description links changed) or UNCHANGED, so the automation knows what to do.
"""
import json, os, re, subprocess, sys, datetime
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import photos_sync

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'tools', 'build.py')
MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def site_ids():
    """IDs of the apartments registered in the list P of tools/build.py, in order."""
    return re.findall(r"^ dict\(id='([^']+)'", open(BUILD, encoding='utf-8').read(), flags=re.M)


def money(v):
    if v is None or str(v).strip() == '':
        return None
    if isinstance(v, (int, float)):
        return round(float(v), 2)
    t = str(v).replace('R$', '').replace(' ', '').strip()
    if ',' in t:
        t = t.replace('.', '').replace(',', '.')
    elif re.fullmatch(r'\d{1,3}(\.\d{3})+', t):  # "3.490" = três mil quatrocentos e noventa
        t = t.replace('.', '')
    return round(float(t), 2)


def norm(v):
    v = str(v).strip().lower()
    return 'Alugado' if v.startswith(('alugad', 'locad')) else 'Disponível'


def drive_files(obj, out=None):
    """Collect every Drive file object found anywhere inside the JSON."""
    out = [] if out is None else out
    if isinstance(obj, dict):
        if obj.get('id') and obj.get('parentId') and obj.get('createdTime'):
            if not obj.get('trashed'):
                out.append(obj)
        else:
            for v in obj.values():
                drive_files(v, out)
    elif isinstance(obj, list):
        for v in obj:
            drive_files(v, out)
    return out


def pick(files, current, seen):
    """Return (chosen id, newest createdTime) following the rule in the module docstring."""
    files = sorted(files, key=lambda f: f['createdTime'])
    newest = files[-1]
    ids = [f['id'] for f in files]
    if seen and newest['createdTime'] > seen:
        return newest['id'], newest['createdTime']
    if current in ids:
        return current, max(newest['createdTime'], seen or '')
    return newest['id'], newest['createdTime']


def current_links():
    """Video and description file IDs written in tools/build.py, per apartment."""
    s = open(BUILD, encoding='utf-8').read()
    out = {}
    for block in re.split(r"^ dict\(id='", s, flags=re.M)[1:]:
        pid = block.split("'", 1)[0]
        v = re.search(r"\bv='[^']*/file/d/([^/']+)", block)
        d = re.search(r"\bd='[^']*/file/d/([^/']+)", block)
        out[pid] = {'video': v.group(1) if v else None, 'desc': d.group(1) if d else None}
    return out


def main():
    new = json.loads(sys.argv[1])
    source = sys.argv[2] if len(sys.argv) > 2 else ''
    IDS = site_ids()
    skipped = [k for k in new if k not in IDS]
    if skipped:
        print('FORA_DO_SITE', json.dumps(skipped, ensure_ascii=False))
    path = os.path.join(ROOT, 'tools', 'status.json')
    old = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {'units': {}}
    old_units = {i: old.get('units', {}).get(i, 'Disponível') for i in IDS}
    old_prices = {k: v for k, v in old.get('prices', {}).items() if k in IDS}
    old_media = {k: v for k, v in old.get('media', {}).items() if k in IDS}
    units = dict(old_units)
    prices = {i: dict(old_prices.get(i, {})) for i in IDS}
    media = {i: dict(old_media.get(i, {})) for i in IDS}
    texts, photos = [], []
    for k, v in new.items():
        if k not in IDS:
            continue
        if not isinstance(v, dict):
            v = {'status': v}
        if 'status' in v:
            units[k] = norm(v['status'])
        for f in ('rent', 'condo', 'iptu'):
            if f in v and money(v[f]) is not None:
                prices[k][f] = money(v[f])
    if len(sys.argv) > 3:
        files = drive_files(json.load(open(sys.argv[3], encoding='utf-8')))
        fp = os.path.join(ROOT, 'tools', 'drive_folders.json')
        folders = json.load(open(fp, encoding='utf-8')) if os.path.exists(fp) else {}
        base = current_links()
        has_pdfs = any(f.get('mimeType') == 'application/pdf' for f in files)
        for i in IDS:
            for kind, is_kind in (('video', lambda m: m.startswith('video/')), ('desc', lambda m: m == 'application/pdf')):
                folder = folders.get(i, {}).get(kind)
                found = {f['id']: f for f in files if f['parentId'] == folder and is_kind(str(f.get('mimeType', '')))}
                if not folder:
                    continue
                if not found:
                    # Description folder with no PDF, in a listing that did find PDFs elsewhere (so the
                    # PDF search worked): the site makes its own description PDF.
                    if kind == 'desc' and has_pdfs and media[i].get('desc') != 'gerado':
                        media[i]['desc'] = 'gerado'
                    continue
                cur = media[i].get(kind) or base.get(i, {}).get(kind)
                chosen, seen = pick(list(found.values()), cur, media[i].get(kind + '_seen'))
                media[i][kind], media[i][kind + '_seen'] = chosen, seen
                if kind == 'desc':
                    # A new description PDF, or the same one edited: the text on the site is redone from it.
                    mod = found[chosen].get('modifiedTime', '')
                    before = old_media.get(i, {})
                    if mod and before.get('desc_mod') and (chosen != before.get('desc') or mod != before.get('desc_mod')):
                        texts.append((i, chosen))
                    media[i]['desc_mod'] = mod
        photos = photos_sync.sync(files, IDS, folders)
    prices = {k: v for k, v in prices.items() if v}
    media = {k: v for k, v in media.items() if v}
    listing_changed = units != old_units or prices != old_prices
    links = lambda m: {k: (v.get('video'), v.get('desc')) for k, v in m.items()}
    media_changed = links(media) != links(old_media)
    for i, f in texts:
        print('DESCRICAO', i, f)
    if photos:
        print('FOTOS', ' '.join(photos))
    if not listing_changed and media == old_media and not photos:
        print('UNCHANGED')
        return
    today = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=3)).date()
    data = {'units': units, 'prices': prices, 'media': media,
            'updated': today.isoformat() if listing_changed else old.get('updated', today.isoformat()),
            'source': source if listing_changed else old.get('source', source)}
    json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if listing_changed:
        s = open(BUILD, encoding='utf-8').read()
        pt = f'{today.day} de {MESES[today.month - 1]} de {today.year}'
        en = f'{today.day} {MONTHS[today.month - 1]} {today.year}'
        s = re.sub(r"^ATUALIZADO = \{[^}]*\}", f"ATUALIZADO = {{'pt': '{pt}', 'en': '{en}'}}", s, count=1, flags=re.M)
        open(BUILD, 'w', encoding='utf-8').write(s)
    subprocess.run([sys.executable, '-I', BUILD], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    if listing_changed:
        print('CHANGED', json.dumps(units, ensure_ascii=False))
    elif media_changed or photos or texts:
        print('MEDIA', json.dumps(links(media), ensure_ascii=False))
    else:
        print('UNCHANGED')


if __name__ == '__main__':
    main()
