# Automação diária: status, preços, vídeos, fotos e descrições

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
   (`video` = pasta do vídeo, `fotos` = pasta de fotos, `desc` = pasta onde fica o PDF de descrição).
   Ver "Vídeos, fotos e descrições".

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

## Vídeos, fotos e descrições

Tudo o que muda nas pastas do Drive de um apartamento entra no site sozinho, na rotina do dia seguinte.
As pastas de cada apartamento estão em `tools/drive_folders.json`: `video` (vídeo), `fotos` (fotos) e
`desc` (onde fica o PDF de descrição).

1. Com o conector do Google Drive, faça uma busca só com todas as pastas de `tools/drive_folders.json`
   (as três de cada apartamento):
   `(mimeType contains 'video/' or mimeType contains 'image/' or mimeType = 'application/pdf') and (parentId = '<pasta 1>' or parentId = '<pasta 2>' ...)`,
   com `pageSize` 200.
2. Se a busca devolver `nextPageToken`, busque as outras páginas também (passando o `pageToken`) e grave
   todas as páginas no arquivo, como uma lista com uma resposta por página. Se o arquivo tiver só páginas com
   `nextPageToken`, o script imprime `LISTA_INCOMPLETA` e não mexe em vídeos, fotos e descrições: busque as
   páginas que faltaram e rode de novo.
3. Grave em `/tmp/drive.json` todos os arquivos encontrados, com os campos `id`, `parentId`, `title`,
   `createdTime`, `modifiedTime` e `mimeType` copiados exatamente como vieram (um caractere errado no `id`
   quebra o site). O mais simples é gravar a resposta da busca como veio. Não inclua arquivos com `trashed: true`.
4. Passe `/tmp/drive.json` como terceiro argumento do script (ver "Aplicar").

O que o script faz com a lista:

- Vídeo: um arquivo colocado na pasta depois da última conferência ganha; senão o atual continua
  enquanto existir; se o atual foi apagado, entra o mais recente da pasta.
- Fotos: se alguma foto entrou, saiu, foi trocada ou mudou de nome na pasta, o script baixa a pasta
  inteira e refaz a galeria e as fotos do cartão (`tools/photos_sync.py`). A ordem é a dos números no
  início do nome do arquivo (1.jpg, 2.jpg ... 10.jpg). Fotos pequenas (menos de 1000 px) vão para o fim
  da galeria e fotos repetidas saem. O cartão e o PDF usam as 5 primeiras da galeria. O script imprime
  `FOTOS <ids>`.
- Descrição: se entrou um PDF novo na pasta `desc` ou o PDF atual foi editado, o script imprime
  `DESCRICAO <id> <id do arquivo no Drive>`.

Pasta sem nenhum arquivo do tipo na lista não muda nada. Se a busca do Drive falhar, rode o script sem o
terceiro argumento: status e preços são atualizados e vídeos, fotos e textos ficam como estão.

Depois do script, antes do commit:

- Para cada linha `DESCRICAO <id> <arquivo>`: leia esse PDF com o conector do Google Drive e refaça os
  textos do apartamento em `tools/build.py` (`tag`, `meta` e `perks` na lista `P`; `head`, `intro`,
  `groups` e `amen` em `DET`), em português e em inglês, no mesmo estilo dos outros. Use só o que está no
  PDF e o que já estava no site e o PDF não contradiz. Não invente itens, metragem, vaga coberta ou
  ar-condicionado. Preços sempre da planilha, mesmo que o PDF traga outro valor. Os links de fotos e vídeo
  dentro do PDF não importam: o site usa as pastas de `tools/drive_folders.json`.
- Para cada apartamento em `FOTOS`: abra as fotos do cartão (`images/g/<id>-1.jpg` a `-5.jpg`) e escreva
  em `gal` uma legenda curta para cada uma, na mesma ordem, em português e em inglês, dizendo só o que se
  vê na foto (ex.: "Sala com sofá e TV", "Piscina do condomínio").
- Se houve uma das duas, rode `python3 -I tools/build.py` de novo. Se der erro, desfaça só as mudanças de
  texto e legenda (`git checkout -- tools/build.py`), rode o build de novo e diga no resumo.

O PDF de descrição que o site mostra é gerado pelo próprio site (`descricao/<id>.pdf`), com os textos,
as fotos do cartão e os custos, e é refeito sozinho quando algum deles muda. O commit leva a pasta
`descricao/` junto.

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
6. Inclua o ID em `tools/drive_folders.json` (pasta do vídeo, pasta de fotos e pasta onde fica o PDF) e na tabela
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
- `MEDIA` (só trocou vídeo, fotos ou descrição): commit e push do mesmo jeito, com mensagem dizendo de
  quais unidades. Não avise os corretores.

Fora o que está descrito aqui, não altere mais nada no site. Não responda nem apague e-mails. Não edite a planilha nem o Drive.

## Cadastro de corretores (e-mails de novidades)

O formulário "Receba os apartamentos em primeira mão" (seção Corretores do site) grava no Supabase,
projeto `global-estadia` (ref `bvwrnddfujpkukzwmioz`), tabela `public.corretores_inscritos`.
O site só chama três funções: `inscrever_corretor`, `cancelar_inscricao` e `confirmar_cadastro`. A tabela não pode ser lida pelo site.
O link de descadastro é `https://globalestadia.com.br/sair.html?t=<token_saida>` (inglês: `&l=en`).

Cadastro com e-mail que já está na lista (desde 15/11/2026): o formulário não muda mais o cadastro existente nem reativa
quem saiu. Os dados novos ficam guardados em `pend_dados` com um `pend_token`, e a pessoa dona do e-mail precisa clicar no
link `https://globalestadia.com.br/confirmar.html?t=<pend_token>` (inglês: `&l=en`). O link vale 7 dias. Ao confirmar,
os dados novos entram, o cadastro fica ativo e, se a pessoa tinha saído da lista, recebe as boas-vindas de novo.
No máximo um e-mail de confirmação por dia para o mesmo endereço.

Envio dos e-mails (ATIVO desde 3/11/2026). Roda na mesma rotina diária, pelo Gmail de contato@globalestadia.com.br:
- boas-vindas: todo dia, para quem tem `ativo` e `boas_vindas_em` vazio. Traz os apartamentos disponíveis com
  valores e total mensal, pede para adicionar contato@ aos contatos e tem o link de descadastro. Depois de enviar,
  preenche `boas_vindas_em`. Quem sai da lista e se cadastra de novo recebe as boas-vindas outra vez
  (`inscrever_corretor` limpa `boas_vindas_em` quando reativa o cadastro);
- aviso de mudanças: só quando `sync_status.py` imprimir CHANGED, para os ativos que não receberam as
  boas-vindas na última hora;
- confirmação de cadastro: todo dia, para quem tem `pend_token` preenchido, `pend_enviado_em` vazio e `pend_em` de até 7 dias.
  Vai para o e-mail que já está na lista, com o nome que já estava no cadastro (nunca o nome novo enviado no formulário).
  Depois de enviar, preenche `pend_enviado_em`;
- um e-mail por pessoa (nunca todos em cópia);
- conteúdo do aviso: o que mudou (disponível, alugado, preço), valores com total mensal e o link do apartamento
  (`https://globalestadia.com.br/#<id>`), e no fim o link de descadastro da própria pessoa.
