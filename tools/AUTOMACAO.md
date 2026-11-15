# Automação diária: status, preços, vídeos e descrições

Roda uma vez por dia. Lê três fontes e atualiza o site sozinha.

## Fontes

1. **Planilha** no Google Drive: "Global Estadia - Status dos apartamentos"
   (id `1wOiK030eGdrXZLcPJNKQjzh5Y56CluJegQNUPh5FU1k`). Leia pelas colunas do cabeçalho, não pela posição:
   "ID (não alterar)", "Status" ("Disponível", "Alugado" ou "Locado"), "Aluguel (R$)", "Condomínio (R$)"
   e "IPTU (R$)" (em reais, formato brasileiro). Os preços vêm sempre da planilha.
   Use todas as linhas da planilha. Uma linha cujo ID ainda não existe na lista `P` de `tools/build.py`
   não entra no site: o script avisa na linha `FORA_DO_SITE`. Se uma dessas estiver "Disponível",
   cadastre o apartamento seguindo "Apartamento novo" antes de rodar o script. Linha nova "Alugado"
   ou "Locado" fica fora do site e não precisa de nada.
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
| Vida Plena D98, D98 | vida-plena-d98 |

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

## Apartamento novo

Vale para uma linha "Disponível" da planilha cujo ID não está na lista `P` de `tools/build.py`.

1. No Drive, ache a pasta do apartamento (busque pela "Identificação" da planilha, ex.: "D98"). Ela precisa ter
   o PDF de descrição, a pasta de fotos e a pasta de vídeo com pelo menos um vídeo. Se faltar o PDF ou as
   fotos, não cadastre: diga no resumo o que falta e siga com o resto da rotina.
2. Leia o PDF de descrição. Use só o que está nele e na planilha. Não invente itens, metragem, vaga coberta
   ou ar-condicionado. Preços sempre da planilha, mesmo que o PDF traga outro valor.
3. Baixe as fotos (as pastas são públicas, não precisa de login) para uma pasta vazia fora do repositório,
   com nomes `01.jpg`, `02.jpg`... na ordem da galeria: sala, cozinha, dormitórios, banheiro, depois o condomínio.
   `curl -sSL -o 01.jpg "https://drive.google.com/thumbnail?id=<id do arquivo>&sz=w1600"`
   Abra as fotos para conferir o que cada uma mostra. Deixe de fora fotos repetidas, de cama sem roupa
   de cama ou ilegíveis.
4. `python3 -I tools/photos.py <id> <pasta> <cartão>`, onde `<cartão>` são de 3 a 5 fotos boas e nítidas
   (largura original de 1000 px ou mais), pela posição na ordem, ex.: `1,2,14,18,16`.
5. Em `tools/build.py`, copie o último bloco da lista `P` e o último de `DET` e preencha com os dados do
   apartamento novo, em português e em inglês, no mesmo estilo dos outros. `gal` tem uma legenda para cada
   foto do cartão, na mesma ordem. `f` = link da pasta de fotos, `v` = link do vídeo, `d` = link do PDF.
6. Inclua o ID em `tools/drive_folders.json` (pasta do vídeo e pasta onde fica o PDF) e na tabela
   "Nomes aceitos no assunto" deste arquivo.
7. Rode `python3 -I tools/build.py`. Se der erro, desfaça tudo com `git checkout -- . && git clean -fd images tools`
   e diga no resumo. Se passar, siga para "Aplicar": o script vai imprimir `CHANGED` por causa do preço novo,
   e o apartamento entra no commit e no aviso aos corretores.

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

Fora o que está descrito aqui, não altere mais nada no site. Não responda nem apague e-mails. Não edite a planilha nem o Drive.

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
