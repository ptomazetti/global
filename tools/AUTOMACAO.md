# Automação diária: status, preços, vídeos e descrições

Roda uma vez por dia. Lê três fontes e atualiza o site sozinha.

## Fontes

1. **Planilha** no Google Drive: "Global Estadia - Status dos apartamentos"
   (id `1wOiK030eGdrXZLcPJNKQjzh5Y56CluJegQNUPh5FU1k`). Leia pelas colunas do cabeçalho, não pela posição:
   "ID (não alterar)", "Status" ("Disponível", "Alugado" ou "Locado"), "Aluguel (R$)", "Condomínio (R$)"
   e "IPTU (R$)" (em reais, formato brasileiro). Os preços vêm sempre da planilha.
   Use todas as linhas da planilha. Uma linha cujo ID ainda não existe na lista `P` de `tools/build.py`
   não entra no site: o script avisa na linha `FORA_DO_SITE`. Se uma dessas estiver "Disponível",
   diga no resumo que há um apartamento novo esperando cadastro no site (fotos e textos).
2. **E-mails** recebidos em contato@globalestadia.com.br, de qualquer remetente, com assunto começando por
   `ALUGADO` ou `DISPONÍVEL` (também aceitar `DISPONIVEL`) seguido do nome da unidade.
   Busca no Gmail: `subject:(ALUGADO OR DISPONIVEL OR DISPONÍVEL) newer_than:3d`
3. **Pastas do Google Drive** de cada apartamento, listadas em `tools/drive_folders.json`
   (`video` = pasta do vídeo, `desc` = pasta onde fica o PDF de descrição). Ver "Vídeos e descrições".

## Nomes aceitos no assunto -> ID

| Palavras no assunto | ID |
|---|---|
| Spettacolo, Patriani, 42 (sem J/I) | spettacolo-42 |
| RED, 1401 | red-1401 |
| J42 | alpha-club-j42 |
| Esplanada, 102 | esplanada-102 |
| I41 | alpha-club-i41 |
| Vida Plena C65, C65 | vida-plena-c65 |

Para unidades que não estão nesta tabela, use a coluna "Identificação" da planilha (ex.: D98).
Se o assunto não identificar uma única unidade com certeza, ignore esse e-mail e cite-o no resumo.

## Regra de prioridade

Para cada unidade, vale a ação mais recente: compare a data do e-mail mais recente daquela
unidade com a data de modificação da planilha. Se o e-mail for mais novo, vale o e-mail;
senão vale a planilha.

## Vídeos e descrições

O site aponta para um arquivo específico do Drive. Quando alguém troca o vídeo ou o PDF na pasta,
o arquivo novo tem outro ID, então a rotina procura o arquivo atual de cada pasta todo dia.

1. Com o conector do Google Drive, liste os vídeos de todas as pastas `video` de `tools/drive_folders.json`
   numa busca só: `mimeType contains 'video/' and (parentId = '<pasta 1>' or parentId = '<pasta 2>' ...)`.
2. Liste os PDFs de todas as pastas `desc` do mesmo jeito, com `mimeType = 'application/pdf'`.
3. Se alguma busca devolver `nextPageToken`, busque as outras páginas também.
4. Grave em `/tmp/drive.json` uma lista JSON com um objeto por arquivo encontrado, com os campos
   `id`, `parentId`, `createdTime` e `mimeType` copiados exatamente como vieram (um caractere errado
   no `id` quebra o vídeo no site). Não inclua arquivos com `trashed: true`.
5. Passe `/tmp/drive.json` como terceiro argumento do script (ver "Aplicar").

O script decide sozinho qual arquivo usar: um arquivo colocado na pasta depois da última conferência
ganha; senão o atual continua enquanto existir; se o atual foi apagado, entra o mais recente da pasta.
Pasta sem nenhum arquivo na lista não muda nada. Se a busca do Drive falhar, rode o script sem o
terceiro argumento: status e preços são atualizados e os vídeos ficam como estão.

## Aplicar

```bash
python3 -I tools/sync_status.py '<json>' "<fonte: planilha/e-mail e datas>" /tmp/drive.json
# <json> = {"<id>": {"status": "Disponível"|"Alugado", "rent": "3.490,00", "condo": "615,09", "iptu": "56,30"}, ...}
# com todas as linhas da planilha. status pela regra de prioridade; rent/condo/iptu sempre da planilha.
```

Vale a última linha que o script imprimir:

- `UNCHANGED`: não faça commit nem push.
- `CHANGED` (mudou status ou preço): rode `git add -A && git commit` (mensagem curta dizendo quais
  unidades mudaram) e `git push origin main`. O GitHub Pages publica sozinho. Avise os corretores.
- `MEDIA` (só trocou vídeo ou descrição): commit e push do mesmo jeito, com mensagem dizendo de quais
  unidades. Não avise os corretores.

Não altere mais nada no site. Não responda nem apague e-mails. Não edite a planilha nem o Drive.

## Cadastro de corretores (e-mails de novidades)

O formulário "Receba os apartamentos em primeira mão" (seção Corretores do site) grava no Supabase,
projeto `global-estadia` (ref `bvwrnddfujpkukzwmioz`), tabela `public.corretores_inscritos`.
O site só chama duas funções: `inscrever_corretor` e `cancelar_inscricao`. A tabela não pode ser lida pelo site.
O link de descadastro é `https://globalestadia.com.br/sair.html?t=<token_saida>` (inglês: `&l=en`).

Envio dos e-mails (ATIVO desde 3/11/2026). Roda na mesma rotina diária, pelo Gmail de contato@globalestadia.com.br:
- boas-vindas: todo dia, para quem tem `ativo` e `boas_vindas_em` vazio. Traz os apartamentos disponíveis com
  valores e total mensal, pede para adicionar contato@ aos contatos e tem o link de descadastro. Depois de enviar,
  preenche `boas_vindas_em`. Quem sai da lista e se cadastra de novo recebe as boas-vindas outra vez
  (`inscrever_corretor` limpa `boas_vindas_em` quando reativa o cadastro);
- aviso de mudanças: só quando `sync_status.py` imprimir CHANGED, para os ativos que não receberam as
  boas-vindas na última hora;
- um e-mail por pessoa (nunca todos em cópia);
- conteúdo do aviso: o que mudou (disponível, alugado, preço), valores com total mensal e o link do apartamento
  (`https://globalestadia.com.br/#<id>`), e no fim o link de descadastro da própria pessoa.
