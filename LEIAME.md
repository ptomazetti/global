# Página de imóveis mobiliados · Global Consultancy Partners

O site tem duas versões: português (`index.html`) e inglês (`en/index.html`). As duas são geradas pelo arquivo `tools/build.py`, a partir dos mesmos dados. Edite o bloco CONFIGURACAO no topo e rode:

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

## Textos em dois idiomas
Cada texto tem a versão `pt` e `en`. Ao trocar um texto ou adicionar um apartamento, preencha os dois idiomas. A data em `ATUALIZADO` também tem as duas versões.

## Vídeos dentro do site
Coloque o arquivo em `videos/<id>.mp4` (ex.: `videos/vida-plena-c65.mp4`) e rode `python3 -I tools/build.py`.
O botão "Ver vídeo" passa a tocar o vídeo no próprio site, sem abrir o Google Drive.
Use MP4 (H.264), até uns 20 MB por vídeo.
