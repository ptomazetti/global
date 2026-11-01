# Página de imóveis mobiliados · Global Consultancy Partners

A página é gerada pelo arquivo `tools/build.py`. Edite o bloco CONFIGURACAO no topo e rode:

    python3 tools/build.py

## Quando um apartamento for alugado
1. Apague o bloco dele na lista `P` em `tools/build.py`.
2. Mude `ATUALIZADO` para a data de hoje.
3. Rode o comando acima. A contagem ("5 apartamentos") e o "a partir de" se ajustam sozinhos.

## Quando entrar um apartamento novo
Copie um bloco da lista `P`, troque nome, valores e links do Drive, e coloque as fotos em `images/g/` com o nome `<id>-1.jpg`, `<id>-2.jpg`... (e as versões `.webp`).

## Itens prontos para ativar
- `DEPOIMENTOS`: aparece a seção "Quem já mora".
- `ATENDENTE`: aparece "Quem responde no WhatsApp" com nome e foto.
- `FAQ_EXTRA`: novas perguntas no FAQ.
- `AIRBNB_URL`: transforma "Global Flats no Airbnb" em link.
