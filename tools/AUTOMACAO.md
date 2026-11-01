# Automação diária: apartamentos alugados / disponíveis

Roda uma vez por dia. Lê duas fontes e tira do site (ou devolve) as unidades.

## Fontes

1. **Planilha** no Google Drive: "Global Estadia - Status dos apartamentos"
   (id `1wOiK030eGdrXZLcPJNKQjzh5Y56CluJegQNUPh5FU1k`). Coluna A = ID, C = Status
   ("Disponível" ou "Alugado"), D = Aluguel, E = Condomínio, F = IPTU (em reais, formato brasileiro).
   Os preços vêm sempre da planilha.
2. **E-mails** recebidos em contato@globalestadia.com.br, de qualquer remetente, com assunto começando por
   `ALUGADO` ou `DISPONÍVEL` (também aceitar `DISPONIVEL`) seguido do nome da unidade.
   Busca no Gmail: `subject:(ALUGADO OR DISPONIVEL OR DISPONÍVEL) newer_than:3d`

## Nomes aceitos no assunto -> ID

| Palavras no assunto | ID |
|---|---|
| Spettacolo, Patriani, 42 (sem J/I) | spettacolo-42 |
| RED, 1401 | red-1401 |
| J42 | alpha-club-j42 |
| Esplanada, 102 | esplanada-102 |
| I41 | alpha-club-i41 |
| Vida Plena, C65 | vida-plena-c65 |

Se o assunto não identificar uma única unidade com certeza, ignore esse e-mail e cite-o no resumo.

## Regra de prioridade

Para cada unidade, vale a ação mais recente: compare a data do e-mail mais recente daquela
unidade com a data de modificação da planilha. Se o e-mail for mais novo, vale o e-mail;
senão vale a planilha.

## Aplicar

```bash
python3 -I tools/sync_status.py '<json>' "<fonte: planilha/e-mail e datas>"
# <json> = {"<id>": {"status": "Disponível"|"Alugado", "rent": "3.490,00", "condo": "615,09", "iptu": "56,30"}, ...}
# com as 6 unidades. status pela regra de prioridade; rent/condo/iptu sempre da planilha.
```

- Se imprimir `UNCHANGED`: não faça commit nem push.
- Se imprimir `CHANGED`: rode `git add -A && git commit` (mensagem curta dizendo quais
  unidades mudaram) e `git push origin main`. O GitHub Pages publica sozinho.

Não altere mais nada no site. Não responda nem apague e-mails. Não edite a planilha.
