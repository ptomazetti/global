"""Apply apartment availability and rebuild the site.

Usage (from the repo root):
    python3 -I tools/sync_status.py '{"red-1401": "Alugado", "vida-plena-c65": "Disponível"}' "fonte da mudança"

- Writes tools/status.json (only the six known IDs, values "Disponível" or "Alugado").
- If anything changed, updates ATUALIZADO (the "lista atualizada em" date) in tools/build.py
  to today's date in São Paulo and runs tools/build.py.
- Prints CHANGED or UNCHANGED so the automation knows whether to commit.
"""
import json, os, re, subprocess, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDS = ['spettacolo-42', 'red-1401', 'alpha-club-j42', 'esplanada-102', 'alpha-club-i41', 'vida-plena-c65']
MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def norm(v):
    v = str(v).strip().lower()
    return 'Alugado' if v.startswith('alugad') else 'Disponível'


def main():
    new = json.loads(sys.argv[1])
    source = sys.argv[2] if len(sys.argv) > 2 else ''
    unknown = [k for k in new if k not in IDS]
    if unknown:
        sys.exit(f'IDs desconhecidos: {unknown}. Use apenas: {IDS}')
    path = os.path.join(ROOT, 'tools', 'status.json')
    old = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {'units': {}}
    units = {i: old.get('units', {}).get(i, 'Disponível') for i in IDS}
    for k, v in new.items():
        units[k] = norm(v)
    changed = units != {i: old.get('units', {}).get(i, 'Disponível') for i in IDS}
    if not changed:
        print('UNCHANGED')
        return
    today = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=3)).date()
    json.dump({'units': units, 'updated': today.isoformat(), 'source': source}, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    bp = os.path.join(ROOT, 'tools', 'build.py')
    s = open(bp, encoding='utf-8').read()
    pt = f'{today.day} de {MESES[today.month - 1]} de {today.year}'
    en = f'{today.day} {MONTHS[today.month - 1]} {today.year}'
    s = re.sub(r"^ATUALIZADO = \{[^}]*\}", f"ATUALIZADO = {{'pt': '{pt}', 'en': '{en}'}}", s, count=1, flags=re.M)
    open(bp, 'w', encoding='utf-8').write(s)
    subprocess.run([sys.executable, '-I', bp], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    print('CHANGED', json.dumps(units, ensure_ascii=False))


if __name__ == '__main__':
    main()
