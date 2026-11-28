"""Gera a planilha de inscritos do 29º Poker Golden Night a partir do Netlify Forms.
Uso: python3 lista_inscritos.py <pasta_de_saida>
O token do Netlify é injetado pelo proxy do ambiente (cabeçalho Authorization)."""
import json, sys, urllib.request, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SITE = "2586bae3-e782-4bfc-a802-1844e25ee284"
BRT = datetime.timezone(datetime.timedelta(hours=-3))

def buscar():
    subs, page = [], 1
    while True:
        req = urllib.request.Request(
            f"https://api.netlify.com/api/v1/sites/{SITE}/submissions?per_page=100&page={page}",
            headers={"Authorization": "Bearer proxy-injected"})
        lote = json.load(urllib.request.urlopen(req, timeout=30))
        subs += lote
        if len(lote) < 100:
            return subs
        page += 1

def main(saida):
    subs = sorted(buscar(), key=lambda s: s["created_at"])
    hoje = datetime.datetime.now(BRT)
    wb = Workbook(); ws = wb.active; ws.title = "Inscritos"
    ws["A1"] = "29º Poker Golden Night: lista de inscritos"
    ws["A1"].font = Font(bold=True, size=14)
    ws["A2"] = f"Atualizada em {hoje:%d/%m/%Y às %Hh%M}. Total: {len(subs)} inscrito(s)."
    cab = ["Nº", "Nome", "WhatsApp", "Pix", "Recado", "Data da inscrição"]
    ws.append([]); ws.append(cab)
    borda = Border(*(Side(style="thin", color="BBBBBB"),) * 4)
    for c in ws[4]:
        c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="D41F26")
        c.alignment = Alignment(vertical="center"); c.border = borda
    pagos = 0
    for i, s in enumerate(subs, 1):
        d = s.get("data") or {}
        quando = datetime.datetime.fromisoformat(s["created_at"].replace("Z", "+00:00")).astimezone(BRT)
        pix = d.get("Pix", "")
        pagos += pix.startswith("Sim")
        ws.append([i, d.get("Nome", ""), d.get("WhatsApp", ""), pix, d.get("Recado", ""), quando.strftime("%d/%m/%Y %H:%M")])
        for c in ws[ws.max_row]:
            c.border = borda; c.alignment = Alignment(vertical="top", wrap_text=True)
    ws.append([]); ws.append(["", f"Disseram que já pagaram: {pagos}", "", f"Ainda vão pagar: {len(subs) - pagos}"])
    ws[ws.max_row][1].font = Font(bold=True); ws[ws.max_row][3].font = Font(bold=True)
    for col, w in zip(range(1, 7), [6, 32, 18, 30, 40, 18]):
        ws.column_dimensions[get_column_letter(col)].width = w
    ws.freeze_panes = "A5"
    nome = f"{saida}/Inscritos_Poker_Golden_Night_{hoje:%d-%m}.xlsx"
    wb.save(nome)
    print(json.dumps({"arquivo": nome, "total": len(subs), "pagos": pagos, "data": f"{hoje:%d/%m/%Y}"}, ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
