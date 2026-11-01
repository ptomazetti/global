"""Gera index.html (portugues) e en/index.html (ingles).
Rode a partir da raiz do repositorio:  python3 tools/build.py
"""
from urllib.parse import quote
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTOS = json.load(open(os.path.join(ROOT, 'tools', 'photos.json'))) if os.path.exists(os.path.join(ROOT, 'tools', 'photos.json')) else {}

# ===== CONFIGURACAO: edite aqui =====================================
SITE = 'https://globalestadia.com.br'
EMAIL = 'contato@globalestadia.com.br'
WA = '5515997470301'
WA_SHOW = '+55 (15) 99747-0301'
CNPJ = '50.945.139/0001-86'
ATUALIZADO = {'pt': '1 de novembro de 2026', 'en': '1 November 2026'}  # mude sempre que um imovel entrar ou sair
AIRBNB_URL = {'pt': 'https://www.airbnb.com.br/users/profile/1779247085187681939', 'en': 'https://www.airbnb.com/users/profile/1779247085187681939'}   # perfil Global Flats no Airbnb
ATENDENTE = {}    # ex.: {'nome': 'Paula', 'foto': 'images/paula.jpg'}
# Avaliações reais do perfil Global Flats no Airbnb (copiadas do perfil público).
DEPOIMENTOS = [
    {'texto': {'pt': 'Excelente experiência! O flat é muito confortável, bem equipado, limpo e exatamente como nas fotos. A localização também é ótima e facilita bastante a estadia. Tudo muito organizado e pensado nos detalhes. Recomendo e certamente voltaria!',
               'en': 'Excellent experience! The flat is very comfortable, well equipped, clean and exactly as in the photos. The location is great too and makes the stay much easier. Everything is well organised and thought through. I recommend it and would definitely come back!'},
     'nome': 'Raffa', 'cidade': 'São Paulo', 'data': {'pt': 'outubro de 2026', 'en': 'October 2026'}},
    {'texto': {'pt': 'Ótimo studio para hospedagem.', 'en': 'Great studio for a stay.'},
     'nome': 'Daniel', 'cidade': 'Espírito Santo do Pinhal', 'data': {'pt': 'outubro de 2026', 'en': 'October 2026'}},
    {'texto': {'pt': 'Excelente estadia.', 'en': 'Excellent stay.'},
     'nome': 'João', 'cidade': '', 'data': {'pt': 'outubro de 2026', 'en': 'October 2026'}},
]
FAQ_EXTRA = [     # (pergunta, resposta) em cada idioma
    ({'pt': 'Tem vaga de garagem?', 'en': 'Is there parking?'},
     {'pt': 'O Spettacolo Patriani tem 2 vagas cobertas e depósito de 10 m². O Alpha Club I41 e o Residencial Esplanada têm 1 vaga cada. Para os outros apartamentos, confirme pelo WhatsApp.',
      'en': 'Spettacolo Patriani has 2 covered parking spaces and a 10 m² storage room. Alpha Club I41 and Residencial Esplanada have 1 space each. For the other apartments, please confirm on WhatsApp.'}),
    ({'pt': 'Os apartamentos têm ar-condicionado?', 'en': 'Do the apartments have air conditioning?'},
     {'pt': 'O Alpha Club J42 tem ar-condicionado de 12.000 BTUs na suíte. O Residencial Esplanada tem ar-condicionado de 12.000 BTUs na sala. O Alpha Club I41 tem ventilador de teto na suíte.',
      'en': 'Alpha Club J42 has 12,000 BTU air conditioning in the master bedroom. Residencial Esplanada has 12,000 BTU air conditioning in the living room. Alpha Club I41 has a ceiling fan in the master bedroom.'}),
    ({'pt': 'Os condomínios têm área de lazer?', 'en': 'Do the buildings have leisure facilities?'},
     {'pt': 'Sim. O Spettacolo Patriani tem piscina com raia, SPA com hidromassagem, sauna, academia, espaço Pilates, salão de festas, quadra de tênis e brinquedoteca. O Alpha Club e o Residencial Esplanada são condomínios clube, e o Vida Plena tem lazer completo.',
      'en': 'Yes. Spettacolo Patriani has a lap pool, spa with hot tub, sauna, gym, Pilates studio, party room, tennis court and kids’ playroom. Alpha Club and Residencial Esplanada are club-style complexes, and Vida Plena has full leisure facilities.'}),
    ({'pt': 'Sou corretor. Posso levar meu cliente para visitar?', 'en': 'I am a real estate agent. Can I bring my client to visit?'},
     {'pt': 'Sim. Envie em uma única mensagem: nome, RG, CRECI, imóvel, dia e horário pretendido. O botão na seção Corretores já abre o WhatsApp com esses campos.',
      'en': 'Yes. Send everything in one message: name, ID (RG), CRECI licence, apartment, and preferred day and time. The button in the Agents section opens WhatsApp with these fields ready.'}),
]
# ====================================================================

P = [
 dict(id='spettacolo-42', beds=0, name='Spettacolo Patriani', rent=3490, condo=615.09, iptu=56.30,
  tag={'pt': 'Studio alto padrão', 'en': 'Premium studio'},
  meta={'pt': 'Apto. 42 · 76 m² de área total', 'en': 'Apt. 42 · 76 m² total area'},
  perks={'pt': ['2 garagens cobertas e depósito de 10 m²', 'Varanda panorâmica, cama box Queen', 'Piscina com raia, SPA, sauna e academia'],
         'en': ['2 covered parking spaces and 10 m² storage', 'Panoramic balcony, Queen bed', 'Lap pool, spa, sauna and gym']},
  gal={'pt': ['Sala com vista pela varanda panorâmica', 'Sala de estar com sofá e poltronas', 'Cozinha com armários planejados e cooktop', 'SPA com hidromassagem do condomínio', 'Fachada do Spettacolo Patriani'],
       'en': ['Living room with panoramic balcony view', 'Living room with sofa and armchairs', 'Kitchen with built-in cabinets and cooktop', 'Building spa with hot tub', 'Spettacolo Patriani entrance']},
  f='https://drive.google.com/drive/folders/1q39K2Jp_P_wErO56gb_jWGZT09iCpRCm?usp=sharing',
  v='https://drive.google.com/file/d/1kIOwgRGXJtbiDFe1ojhOEfEv-8Zx6k-m/view',
  d='https://drive.google.com/file/d/1akjtOVeacGJNRz2Ihp5uc-KQfwCBWlxQ/view?usp=drive_link'),
 dict(id='red-1401', beds=0, name='RED Studio', rent=3490, condo=692.30, iptu=68.71,
  tag={'pt': 'Studio alto padrão', 'en': 'Premium studio'},
  meta={'pt': 'Apto. 1401 · 56 m² · 14º andar · Jardim América', 'en': 'Apt. 1401 · 56 m² · 14th floor · Jardim América'},
  perks={'pt': ['Varanda gourmet envidraçada com vista para o pôr do sol', '2 vagas de garagem cobertas', 'Internet de 500 Mega, utensílios e enxoval inclusos'],
         'en': ['Glazed balcony with sunset views', '2 covered parking spaces', '500 Mbps internet, kitchenware and linens included']},
  gal={'pt': ['Sala e cozinha integradas com mesa de jantar', 'Varanda envidraçada com vista para o pôr do sol', 'Dormitório com cama Queen', 'Cozinha com cooktop e geladeira duplex'],
       'en': ['Open-plan living room and kitchen with dining table', 'Glazed balcony with sunset view', 'Bedroom with Queen bed', 'Kitchen with cooktop and double-door fridge']},
  f='https://drive.google.com/drive/folders/1IaoP91_8A-CrCQQCnj8nSOvl6uHE0SlI?usp=drive_link',
  v='https://drive.google.com/file/d/1hH0mENGtc03eREHB4j0y6fiUj6KcpUKx/view',
  d='https://drive.google.com/file/d/1I3UIwxGQJ1ij7WcLU8AIxy1giDVVRke6/view?usp=sharing'),
 dict(id='alpha-club-j42', beds=2, name='Alpha Club J42', rent=2890, condo=464.19, iptu=158.00,
  tag={'pt': '2 dormitórios c/ suíte', 'en': '2 bedrooms, 1 en suite'},
  meta={'pt': 'Apto. 42 · Bloco J · Campolim', 'en': 'Apt. 42 · Block J · Campolim'},
  perks={'pt': ['Ar-condicionado 12.000 BTUs na suíte', 'Cama box Queen, Smart TV, cortina blackout', 'Varanda gourmet, condomínio clube'],
         'en': ['12,000 BTU air conditioning in the master bedroom', 'Queen bed, Smart TV, blackout curtains', 'Barbecue balcony, club-style complex']},
  gal={'pt': ['Sala com bar iluminado e bancada', 'Cozinha com geladeira, fogão e micro-ondas'],
       'en': ['Living room with lit bar and counter', 'Kitchen with fridge, stove and microwave']},
  f='https://drive.google.com/drive/folders/1bPidYHmKlhAE6bBfmmKMkpROLZA144Wz?usp=drive_link',
  v='https://drive.google.com/file/d/1hPaG3fANuAu8tYZfaidFGuLrdw7M8XMh/view',
  d='https://drive.google.com/file/d/1W3QlSmMlkzd-SnY9_mjDsCZN_WANdPRY/view?usp=sharing'),
 dict(id='esplanada-102', beds=3, name='Residencial Esplanada', rent=2890, condo=500.00, iptu=105.33,
  tag={'pt': '3 dormitórios', 'en': '3 bedrooms'},
  meta={'pt': 'Apto. 102 · Bloco 2', 'en': 'Apt. 102 · Block 2'},
  perks={'pt': ['Cozinha equipada, geladeira 440 L, cooktop e forno', 'Máquina lava e seca, ar-condicionado na sala', '1 vaga, condomínio clube'],
         'en': ['Equipped kitchen, 440 L fridge, cooktop and oven', 'Washer-dryer, air conditioning in the living room', '1 parking space, club-style complex']},
  gal={'pt': ['Sala integrada com mesa de jantar', 'Cozinha com geladeira e micro-ondas', 'Dormitório com armário planejado'],
       'en': ['Open-plan living and dining room', 'Kitchen with fridge and microwave', 'Bedroom with built-in wardrobe']},
  f='https://drive.google.com/drive/folders/1A19Eb5ZPVLWmBcxqc6R4a2GPwvbjgVFB?usp=drive_link',
  v='https://drive.google.com/file/d/1fnlMgA-zpWuqXb1aKqtkJaMqdwAT2hpM/view',
  d='https://drive.google.com/file/d/19NxWZqBZ20AZ7AQVyDnz_o85rwfdnqPo/view?usp=sharing'),
 dict(id='alpha-club-i41', beds=2, name='Alpha Club I41', rent=2790, condo=497.77, iptu=158.12,
  tag={'pt': '2 dormitórios c/ suíte', 'en': '2 bedrooms, 1 en suite'},
  meta={'pt': 'Apto. 41 · Bloco I · Campolim', 'en': 'Apt. 41 · Block I · Campolim'},
  perks={'pt': ['Dois quartos com cama box de casal', 'Mesa de jantar para 4 lugares', 'Varanda gourmet, 1 vaga, condomínio clube'],
         'en': ['Two bedrooms with double beds', 'Dining table for 4', 'Barbecue balcony, 1 parking space, club-style complex']},
  gal={'pt': ['Sala com sofá e Smart TV', 'Cozinha equipada com máquina de lavar', 'Academia do condomínio', 'Piscina do condomínio'],
       'en': ['Living room with sofa and Smart TV', 'Equipped kitchen with washing machine', 'Building gym', 'Building pool']},
  f='https://drive.google.com/drive/folders/1UxoTaZttGauF5RwCaPovwjylUFDpiMxK?usp=drive_link',
  v='https://drive.google.com/file/d/1BU5odrV48fFY614L7pn84adMBT3lnjbk/view',
  d='https://drive.google.com/file/d/1PBosWcqSD6zJ6Efxw_TIPX-IsAMZ3zzL/view?usp=drive_link'),
 dict(id='vida-plena-c65', beds=2, name='Vida Plena C65', rent=2790, condo=406.42, iptu=61.84,
  tag={'pt': '2 dormitórios', 'en': '2 bedrooms'},
  meta={'pt': 'Apto. 65 · Bloco C · Campolim', 'en': 'Apt. 65 · Block C · Campolim'},
  perks={'pt': ['Armários planejados em todos os cômodos', 'Bancada para home office, iluminação LED', 'Condomínio com lazer completo'],
         'en': ['Built-in cabinets in every room', 'Home office desk, LED lighting', 'Full leisure facilities']},
  gal={'pt': ['Sala com mesa de jantar', 'Cozinha com geladeira, fogão e micro-ondas', 'Dormitório com cama box e armário'],
       'en': ['Living room with dining table', 'Kitchen with fridge, stove and microwave', 'Bedroom with bed and wardrobe']},
  f='https://drive.google.com/drive/folders/1qV2qAFvA47z2pMG8QX_9GhA8e6oTtLZb?usp=drive_link',
  v='https://drive.google.com/file/d/1GGAoURs9YMaWWMq_5RUFMra8ltsm5l6Y/view',
  d='https://drive.google.com/file/d/1J17liUYRHgMADoPXDzAqgiYSOjdORVh1/view?usp=sharing'),
]
PID = {p["id"]: p for p in P}

DET = {
 'spettacolo-42': {
  'pt': dict(head='Studio alto padrão com varanda panorâmica',
    intro='76 m² de área total, ampla varanda panorâmica, 2 vagas cobertas e depósito de 10 m².',
    groups=[('Ambientes', ['Armários planejados em todos os ambientes', 'Cama box Queen, sofá-cama e poltronas', 'Mesa de jantar e bancada para home office', 'Cortinas e decoração completa']),
            ('Cozinha', ['Cooktop, coifa e geladeira']),
            ('Garagem', ['2 vagas cobertas', 'Depósito de 10 m²'])],
    amen=['Piscina com raia', 'SPA com hidromassagem', 'Sauna', 'Academia completa', 'Espaço Pilates', 'Salão de festas com pista de dança', 'Espaço grill', 'Espaço de jogos', 'Espaço beauty care', 'Quadra de tênis', 'Brinquedoteca']),
  'en': dict(head='Premium studio with a panoramic balcony',
    intro='76 m² total area, a large panoramic balcony, 2 covered parking spaces and a 10 m² storage room.',
    groups=[('Living spaces', ['Built-in cabinets throughout', 'Queen bed, sofa bed and armchairs', 'Dining table and home office desk', 'Curtains and full decor']),
            ('Kitchen', ['Cooktop, range hood and fridge']),
            ('Parking', ['2 covered parking spaces', '10 m² storage room'])],
    amen=['Lap pool', 'Spa with hot tub', 'Sauna', 'Fully equipped gym', 'Pilates studio', 'Party room with dance floor', 'Grill area', 'Games room', 'Beauty care room', 'Tennis court', 'Kids’ playroom'])},
 'red-1401': {
  'pt': dict(head='Studio de 56 m² no 14º andar, com vista para o pôr do sol',
    intro='No RED Studio, Jardim América, a 5 minutos do Shopping Iguatemi. Último andar, com varanda gourmet envidraçada de 12 m², 2 vagas cobertas, internet de 500 Mega e tudo para o dia a dia.',
    groups=[('Ambientes', ['Varanda gourmet envidraçada de 12 m²', 'Smart TV 50" com giro de 360°, sofá, mesa e banquetas', 'Bar espelhado com iluminação especial', 'Bancada de trabalho e armários planejados', 'Teto em gesso, cortinas sob medida e iluminação direcionada']),
            ('Dormitório', ['Cama Queen box com molas ensacadas']),
            ('Cozinha', ['Cooktop, forno elétrico e coifa', 'Micro-ondas e geladeira duplex Frost Free']),
            ('Garagem', ['2 vagas cobertas']),
            ('Incluso no aluguel', ['Internet de 500 Mega', 'Utensílios de cozinha, jogo de panelas, torradeira e cafeteira Nespresso', 'Enxoval de cama, mesa e banho', 'Secador de cabelo, vaporizador de roupas e aspirador de pó'])],
    amen=['Piscina com raia', 'Academia', 'Lavanderia coletiva', '2 salões de festas', 'Espaço grill', 'Espaço home office', 'Espaço beauty', 'Vending machines', 'Portaria 24h', 'Lobby']),
  'en': dict(head='56 m² studio on the 14th floor, with sunset views',
    intro='At RED Studio in Jardim América, 5 minutes from Shopping Iguatemi. Top floor, with a 12 m² glazed balcony, 2 covered parking spaces, 500 Mbps internet and everything for daily life.',
    groups=[('Living spaces', ['12 m² glazed balcony', '50" Smart TV on a 360° swivel, sofa, table and bar stools', 'Mirrored bar with feature lighting', 'Work desk and built-in cabinets', 'Plaster ceiling, made-to-measure curtains and spot lighting']),
            ('Bedroom', ['Queen bed with pocket springs']),
            ('Kitchen', ['Cooktop, electric oven and range hood', 'Microwave and double-door frost-free fridge']),
            ('Parking', ['2 covered parking spaces']),
            ('Included in the rent', ['500 Mbps internet', 'Kitchenware, pans, toaster and Nespresso machine', 'Bed, table and bath linens', 'Hair dryer, garment steamer and vacuum cleaner'])],
    amen=['Lap pool', 'Gym', 'Shared laundry', '2 party rooms', 'Grill area', 'Home office space', 'Beauty room', 'Vending machines', '24-hour concierge', 'Lobby'])},
 'alpha-club-j42': {
  'pt': dict(head='2 dormitórios com suíte e ar-condicionado',
    intro='No Alpha Club, no Campolim. Suíte com cama Queen de molas ensacadas e ar-condicionado de 12.000 BTUs.',
    groups=[('Ambientes', ['Armários planejados em todos os cômodos', 'Sofá, banquetas e mesa de jantar', 'Bancada para home office', 'Cortina blackout', 'Varanda gourmet']),
            ('Cozinha e serviço', ['Fogão, coifa, micro-ondas e geladeira', 'Máquina de lavar']),
            ('Tecnologia e estilo', ['Smart TV Samsung', 'Bar iluminado', 'Iluminação 100% LED'])],
    amen=['Condomínio clube']),
  'en': dict(head='2 bedrooms with en suite and air conditioning',
    intro='At Alpha Club in Campolim. The master bedroom has a Queen bed with pocket springs and 12,000 BTU air conditioning.',
    groups=[('Living spaces', ['Built-in cabinets in every room', 'Sofa, bar stools and dining table', 'Home office desk', 'Blackout curtains', 'Barbecue balcony']),
            ('Kitchen and laundry', ['Stove, range hood, microwave and fridge', 'Washing machine']),
            ('Tech and style', ['Samsung Smart TV', 'Lit bar', '100% LED lighting'])],
    amen=['Club-style complex'])},
 'esplanada-102': {
  'pt': dict(head='3 dormitórios com cozinha completa',
    intro='No Residencial Esplanada, Bloco 2. O único de 3 dormitórios da lista, com ar-condicionado na sala e lavanderia completa.',
    groups=[('Ambientes', ['Dormitórios, cozinha e banheiro com móveis planejados', 'Sala com ar-condicionado de 12.000 BTUs', 'Smart TV, sofá e mesa com cadeiras']),
            ('Cozinha', ['Fogão, cooktop, forno elétrico e coifa', 'Micro-ondas', 'Geladeira Frost Free Duplex de 440 L']),
            ('Lavanderia', ['Área de serviço completa com máquina lava e seca']),
            ('Garagem', ['1 vaga'])],
    amen=['Condomínio clube']),
  'en': dict(head='3 bedrooms with a fully equipped kitchen',
    intro='At Residencial Esplanada, Block 2. The only 3-bedroom on our list, with air conditioning in the living room and a full laundry.',
    groups=[('Living spaces', ['Built-in furniture in the bedrooms, kitchen and bathroom', 'Living room with 12,000 BTU air conditioning', 'Smart TV, sofa, table and chairs']),
            ('Kitchen', ['Stove, cooktop, electric oven and range hood', 'Microwave', '440 L frost-free double-door fridge']),
            ('Laundry', ['Full laundry area with washer-dryer']),
            ('Parking', ['1 parking space'])],
    amen=['Club-style complex'])},
 'alpha-club-i41': {
  'pt': dict(head='2 dormitórios com suíte e varanda gourmet',
    intro='No Alpha Club, no Campolim. Dois quartos com cama de casal e uma vaga de garagem.',
    groups=[('Suíte', ['Cama box de casal', 'Armário e ventilador de teto']),
            ('Segundo quarto', ['Cama box de casal e armário']),
            ('Sala e varanda', ['Sofá e TV', 'Mesa de jantar para 4 lugares', 'Varanda gourmet']),
            ('Cozinha e serviço', ['Armários planejados', 'Fogão, micro-ondas e geladeira', 'Máquina de lavar']),
            ('Garagem', ['1 vaga'])],
    amen=['Condomínio clube']),
  'en': dict(head='2 bedrooms with en suite and a barbecue balcony',
    intro='At Alpha Club in Campolim. Two bedrooms with double beds and one parking space.',
    groups=[('Master bedroom', ['Double bed', 'Wardrobe and ceiling fan']),
            ('Second bedroom', ['Double bed and wardrobe']),
            ('Living room and balcony', ['Sofa and TV', 'Dining table for 4', 'Barbecue balcony']),
            ('Kitchen and laundry', ['Built-in cabinets', 'Stove, microwave and fridge', 'Washing machine']),
            ('Parking', ['1 parking space'])],
    amen=['Club-style complex'])},
 'vida-plena-c65': {
  'pt': dict(head='2 dormitórios com espaço para home office',
    intro='No Vida Plena, no Campolim, em condomínio com lazer completo.',
    groups=[('Ambientes', ['Armários planejados em todos os cômodos', 'Cama box de casal em um quarto e de solteiro no outro', 'Sofá e mesa de jantar', 'Bancada para home office', 'Cortinas']),
            ('Cozinha e serviço', ['Fogão, micro-ondas e geladeira', 'Máquina de lavar']),
            ('Tecnologia', ['TV', 'Iluminação 100% LED'])],
    amen=['Lazer completo']),
  'en': dict(head='2 bedrooms with a home office corner',
    intro='At Vida Plena in Campolim, in a building with full leisure facilities.',
    groups=[('Living spaces', ['Built-in cabinets in every room', 'Double bed in one bedroom, single bed in the other', 'Sofa and dining table', 'Home office desk', 'Curtains']),
            ('Kitchen and laundry', ['Stove, microwave and fridge', 'Washing machine']),
            ('Tech', ['TV', '100% LED lighting'])],
    amen=['Full leisure facilities'])},
}

T = {
 'pt': dict(
  html_lang='pt-BR', og_locale='pt_BR',
  title='Apartamentos mobiliados em Sorocaba a partir de {MIN} | Global Estadia',
  desc='{N} apartamentos mobiliados prontos para morar em Sorocaba, de studio a 3 dormitórios. Aluguel a partir de {MIN}. Agende sua visita pelo WhatsApp.',
  og_title='Apartamentos mobiliados em Sorocaba, prontos para morar',
  og_desc='{N} apartamentos disponíveis, de studio a 3 dormitórios. Aluguel a partir de {MIN}. Agende sua visita pelo WhatsApp.',
  og_alt='Sala mobiliada de um dos apartamentos da Global',
  nav_label='Principal', nav=['Apartamentos', 'Como funciona', 'Avaliações', 'Dúvidas', 'Corretores'],
  lang_label='Idioma', cta_short='Agendar visita', cta_long='Agendar visita pelo WhatsApp',
  eyebrow='Locação mobiliada em Sorocaba',
  h1='Apartamento mobiliado. Você só traz a mala.',
  lead='Prontos para morar, de studio a 3 dormitórios. Condomínios com lazer e aluguel a partir de {MIN}. Visite antes de decidir.',
  see_all='Ver apartamentos',
  proof=['Chaves em até 2 dias após a documentação', 'Aceita animais de estimação', 'Pintado e higienizado a cada locação', '3 opções de garantia'],
  hero_alt='Sala mobiliada do Spettacolo Patriani com sofá, poltronas e tapete',
  badge='disponíveis hoje', updated='Lista atualizada em {DATE}',
  agent='Quem responde no WhatsApp:',
  stats=[('{N}', 'apartamentos disponíveis'), ('{MIN}', 'aluguel a partir de'), ('2 dias', 'para pegar as chaves'), ('Pets', 'são bem-vindos')],
  filters=['Todos', 'Studio', '2 dormitórios', '3 dormitórios'], sort_label='Ordenar', sort_opts=['Maior preço', 'Menor preço'],
  amen_eyebrow='Lazer', amen_h='Mais do que um apartamento', amen_p='Piscina, academia, SPA e áreas de convivência nos condomínios. Tudo a poucos passos da sua porta.',
  amen_tiles=[('alpha-club-i41-4', 'Piscina', 'Alpha Club'), ('alpha-club-i41-3', 'Academia', 'Alpha Club'), ('spettacolo-42-4', 'SPA com hidromassagem', 'Spettacolo Patriani')],
  list_eyebrow='Disponíveis agora',
  list_h='Escolha o seu e marque a visita',
  list_p='Valores completos à vista: aluguel, condomínio e IPTU. Sem surpresa no contrato.',
  photos_of='Fotos do {name}', prev='Foto anterior', next='Próxima foto',
  per_month=' /mês', total_with='{v} no total, com condomínio e IPTU', condo='Condomínio', iptu='IPTU', total='Total mensal',
  visit_this='Quero visitar este', l_photos='Fotos', l_video='Vídeo', l_desc='Fotos e detalhes', l_desc_n='{n} fotos e detalhes', share='Compartilhar', share_ok='Link copiado', photo_n='foto {i} de {n}', mail_subj='Quero agendar uma visita', mail_ok='E-mail copiado: ', share_h='Compartilhar este apartamento', share_copy='Copiar link', share_mail='E-mail', share_txt='{name} · {tag} · {rent}/mês. Veja fotos e detalhes:', all_photos='Todas as fotos', menu='Menu', menu_nav='Navegue', menu_apts='Apartamentos', fullscreen='Tela cheia', video_btn='Ver vídeo', d_costs='Custos mensais', d_rent='Aluguel', d_close='Fechar', d_amen='Condomínio', d_full='Descrição original', d_note='Para agendar, envie em uma única mensagem: nome, apartamento, dia e horário. Corretores: incluam RG e CRECI.',
  steps_h='Da visita às chaves em 3 passos',
  steps=[('Escolha e visite', 'Toque em "Quero visitar este" no apartamento. A mensagem já vai pronta no WhatsApp, com o nome do imóvel.'),
         ('Escolha a garantia', 'Seguro fiança, caução de 3 aluguéis ou fiador. Você usa a que for mais simples para você.'),
         ('Entre com a mala', 'As chaves saem em até 2 dias depois da documentação.')],
  cmp_a='Alugar um apartamento vazio', cmp_a_list=['Comprar sofá, cama, mesa e cortinas', 'Comprar geladeira, fogão, micro-ondas e máquina de lavar', 'Pagar frete, montagem e instalação', 'Semanas até a casa ficar pronta'],
  cmp_b='Alugar com a Global', cmp_b_list=['Móveis e armários planejados já instalados', 'Eletrodomésticos funcionando', 'Apartamento pintado e higienizado', 'Você muda sem esperar móveis chegarem'],
  quotes_h='Avaliações de hóspedes no Airbnb', host_h='Quem cuida dos apartamentos', host_items=['Gestor imobiliário', 'Atende em português, inglês e espanhol', 'Identidade verificada no Airbnb'], quotes_more='Ver todas no Airbnb', quotes_tr='',
  faq_h='Perguntas antes de visitar',
  faq=[('Qual é o prazo do contrato e quais garantias vocês aceitam?', 'O contrato é de 30 meses, e depois de 12 meses você pode sair sem multa. Aceitamos seguro fiança, caução de 3 aluguéis ou fiador.'),
       ('O que está incluso no valor?', 'O aluguel. Condomínio e IPTU são cobrados à parte, e cada apartamento mostra o total mensal. Luz e internet ficam no nome do inquilino, assim como água e gás quando não estiverem no condomínio. Exceção: no RED Studio, a internet de 500 Mega já está incluída.'),
       ('O que vem no apartamento?', 'Móveis, cozinha equipada e eletrodomésticos. A lista de cada um está em "Fotos e detalhes". A cada nova locação, o apartamento é pintado e higienizado.'),
       ('Aceita animais de estimação?', 'Sim.'),
       ('Tem vaga, ar-condicionado e lazer?', 'Vagas: o Spettacolo Patriani tem 2 cobertas e depósito de 10 m², o RED Studio tem 2 cobertas, e o Alpha Club I41 e o Residencial Esplanada têm 1 cada. Nos outros, confirme pelo WhatsApp. Ar-condicionado: Alpha Club J42 na suíte e Residencial Esplanada na sala. O Alpha Club I41 tem ventilador de teto na suíte. Todos os condomínios têm área de lazer.'),
       ('Como agendo a visita e em quanto tempo recebo as chaves?', 'Pelo {WALINK}: diga o apartamento, o dia e o horário. Se preferir, escreva para {MAILLINK}. Corretores: incluam nome, RG e CRECI na mesma mensagem. As chaves saem em até 2 dias depois da documentação.')],
  short_q='Preciso de uma estadia curta. Vocês têm?', short_a='Sim, para estadias curtas procure por {AIRBNB}.', airbnb='Global Flats no Airbnb', ab_h='Procurando algo por poucos dias?', ab_p='Para estadias curtas, os apartamentos também estão no Airbnb como Global Flats.', ab_btn='Ver no Airbnb', ab_search='Procure por "Global Flats" no Airbnb',
  brk_eyebrow='Para corretores parceiros', brk_h='Feche locação sem montar material.',
  brk_p='Cada apartamento já tem fotos, vídeo e descrição prontos para você enviar ao cliente. Abra "Fotos e detalhes" em cada apartamento ou peça o material completo.',
  brk_box='Para agendar uma visita', brk_send='Envie em uma única mensagem:', brk_chips=['Nome', 'RG', 'CRECI', 'Imóvel', 'Dia e horário'],
  brk_btn='Enviar pedido de visita', brk_small='O botão abre o WhatsApp com esses campos já preenchidos.',
  end_h='Gostou de um? Marque a visita hoje.', end_p='Cada apartamento é único. Quando ele é alugado, sai da lista.',
  foot_tag='Locação de apartamentos mobiliados · Sorocaba', foot_wa='Fale pelo WhatsApp',
  wa_general='Olá! Vi o site da Global e quero agendar uma visita. Meu nome é: ',
  wa_unit='Olá! Vi o site da Global e quero visitar o {name} ({price}). Meu nome é: ',
  wa_broker='Olá! Sou corretor(a) e quero agendar uma visita.\nNome:\nRG:\nCRECI:\nImóvel:\nDia e horário:',
  list_name='Apartamentos mobiliados para locação',
 ),
 'en': dict(
  html_lang='en', og_locale='en_US',
  title='Furnished apartments for rent in Sorocaba, Brazil, from {MIN} | Global Estadia',
  desc='{N} fully furnished apartments ready to move into in Sorocaba, Brazil, from studio to 3 bedrooms. Rent from {MIN} a month. Book a viewing on WhatsApp.',
  og_title='Furnished apartments in Sorocaba, ready to move in',
  og_desc='{N} apartments available, from studio to 3 bedrooms. Rent from {MIN} a month. Book a viewing on WhatsApp.',
  og_alt='Furnished living room in one of the Global apartments',
  nav_label='Main', nav=['Apartments', 'How it works', 'Reviews', 'FAQ', 'Agents'],
  lang_label='Language', cta_short='Book a viewing', cta_long='Book a viewing on WhatsApp',
  eyebrow='Furnished rentals in Sorocaba, Brazil',
  h1='Fully furnished. Just bring your suitcase.',
  lead='Ready to move into, from studio to 3 bedrooms. Buildings with leisure facilities, rent from {MIN} a month. See it before you decide.',
  see_all='See the apartments',
  proof=['Keys within 2 days of your documents', 'Pets welcome', 'Repainted and deep cleaned before every new tenant', '3 rental guarantee options'],
  hero_alt='Furnished living room at Spettacolo Patriani with sofa, armchairs and rug',
  badge='available today', updated='List updated {DATE}',
  agent='Your contact on WhatsApp:',
  stats=[('{N}', 'apartments available'), ('{MIN}', 'rent from'), ('2 days', 'to get your keys'), ('Pets', 'are welcome')],
  filters=['All', 'Studio', '2 bedrooms', '3 bedrooms'], sort_label='Sort', sort_opts=['Highest price', 'Lowest price'],
  amen_eyebrow='Leisure', amen_h='More than an apartment', amen_p='Pools, gyms, spa and shared spaces in the buildings. All just steps from your door.',
  amen_tiles=[('alpha-club-i41-4', 'Pool', 'Alpha Club'), ('alpha-club-i41-3', 'Gym', 'Alpha Club'), ('spettacolo-42-4', 'Spa with hot tub', 'Spettacolo Patriani')],
  list_eyebrow='Available now',
  list_h='Choose yours and book a viewing',
  list_p='Full costs shown upfront: rent, condo fee and property tax (IPTU). No surprises in the contract.',
  photos_of='Photos of {name}', prev='Previous photo', next='Next photo',
  per_month=' /month', total_with='{v} in total, incl. condo fee and IPTU tax', condo='Condo fee', iptu='IPTU tax', total='Total per month',
  visit_this='I want to see this one', l_photos='Photos', l_video='Video', l_desc='Photos and details', l_desc_n='{n} photos and details', share='Share', share_ok='Link copied', photo_n='photo {i} of {n}', mail_subj='I would like to book a viewing', mail_ok='Email copied: ', share_h='Share this apartment', share_copy='Copy link', share_mail='Email', share_txt='{name} · {tag} · {rent}/month. See photos and details:', all_photos='All photos', menu='Menu', menu_nav='Browse', menu_apts='Apartments', fullscreen='Full screen', video_btn='Watch video', d_costs='Monthly costs', d_rent='Rent', d_close='Close', d_amen='Building', d_full='Original description (Portuguese)', d_note='To book, send in one message: your name, the apartment, and day and time. Agents: please include your ID (RG) and CRECI.',
  steps_h='From viewing to keys in 3 steps',
  steps=[('Choose and visit', 'Tap "I want to see this one" on the apartment. WhatsApp opens with your message ready, including the apartment name.'),
         ('Pick your guarantee', 'Rent guarantee insurance (seguro fiança), a deposit of 3 months’ rent (caução) or a guarantor (fiador). Use whichever is easiest for you.'),
         ('Move in with a suitcase', 'You get the keys within 2 days of handing in your documents.')],
  cmp_a='Renting an empty apartment', cmp_a_list=['Buy a sofa, bed, table and curtains', 'Buy a fridge, stove, microwave and washing machine', 'Pay for delivery, assembly and installation', 'Weeks before the place is ready'],
  cmp_b='Renting with Global', cmp_b_list=['Furniture and built-in cabinets already in place', 'Appliances working', 'Apartment repainted and deep cleaned', 'Move in without waiting for furniture'],
  quotes_h='Guest reviews on Airbnb', host_h='Who looks after the apartments', host_items=['Property manager', 'Speaks English, Portuguese and Spanish', 'Identity verified on Airbnb'], quotes_more='See all on Airbnb', quotes_tr='Translated from Portuguese.',
  faq_h='Questions before your viewing',
  faq=[('How long is the lease, and which guarantees do you accept?', 'The lease is 30 months, and after 12 months you can leave without a penalty. We accept rent guarantee insurance (seguro fiança), a deposit of 3 months’ rent (caução) or a guarantor (fiador).'),
       ('What does the price include?', 'The rent. The condo fee and IPTU tax are charged separately, and each apartment shows the monthly total. Electricity and internet go in the tenant’s name, as do water and gas when they are not in the condo fee. Exception: at RED Studio, 500 Mbps internet is already included.'),
       ('What comes with the apartment?', 'Furniture, an equipped kitchen and appliances. The list for each one is under "Photos and details". Before every new tenant, the apartment is repainted and deep cleaned.'),
       ('Are pets allowed?', 'Yes.'),
       ('Is there parking, air conditioning and leisure?', 'Parking: Spettacolo Patriani has 2 covered spaces and a 10 m² storage room, RED Studio has 2 covered spaces, and Alpha Club I41 and Residencial Esplanada have 1 each. For the others, please confirm on WhatsApp. Air conditioning: Alpha Club J42 in the master bedroom and Residencial Esplanada in the living room. Alpha Club I41 has a ceiling fan in the master bedroom. All buildings have leisure facilities.'),
       ('How do I book a viewing, and how soon do I get the keys?', 'On {WALINK}: tell us the apartment, day and time. You can also email {MAILLINK}. Agents: include your name, ID (RG) and CRECI in the same message. Keys are ready within 2 days of receiving your documents.')],
  short_q='I need a short stay. Do you offer that?', short_a='Yes. For short stays, look for {AIRBNB}.', airbnb='Global Flats on Airbnb', ab_h='Looking for just a few days?', ab_p='For short stays, the apartments are also on Airbnb as Global Flats.', ab_btn='View on Airbnb', ab_search='Search "Global Flats" on Airbnb',
  brk_eyebrow='For partner real estate agents', brk_h='Close rentals without building your own material.',
  brk_p='Every apartment already has photos, video and a description ready to send to your client. Open "Photos and details" on each apartment or ask for the full pack.',
  brk_box='To book a viewing', brk_send='Send in one message:', brk_chips=['Name', 'ID (RG)', 'CRECI', 'Apartment', 'Day and time'],
  brk_btn='Send viewing request', brk_small='The button opens WhatsApp with these fields ready to fill in.',
  end_h='Like one? Book your viewing today.', end_p='Every apartment is one of a kind. Once it is rented, it comes off the list.',
  foot_tag='Furnished apartment rentals · Sorocaba, Brazil', foot_wa='Chat on WhatsApp',
  wa_general='Hello! I saw the Global website and would like to book a viewing. My name is: ',
  wa_unit='Hello! I saw the Global website and would like to see {name} ({price}). My name is: ',
  wa_broker='Hello! I am a real estate agent and would like to book a viewing.\nName:\nID (RG):\nCRECI:\nApartment:\nDay and time:',
  list_name='Furnished apartments for rent',
 ),
}

def wa(msg): return f'https://wa.me/{WA}?text={quote(msg)}'
def money(v, lang, cents=True):
    s = f'{v:,.2f}'
    if lang == 'pt':
        s = s.replace(',', 'X').replace('.', ',').replace('X', '.')
    if not cents:
        s = s[:-3]
    return 'R$ ' + s

WA_SVG = open('tools/icons/whatsapp.svg').read().split('d="')[1].split('"')[0]
AB_SVG = open('tools/icons/airbnb.svg').read().split('d="')[1].split('"')[0]
def wai(sz=18): return f'<svg class="logo" width="{sz}" height="{sz}" viewBox="0 0 24 24" aria-hidden="true"><path d="{WA_SVG}"/></svg>'
CAM = '<svg width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>'
PLAY = '<svg width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m10 8 6 4-6 4z"/></svg>'
SHARE = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/></svg>'
DOC = '<svg width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>'
MENU_I = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>'
EXPAND = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>'
CHECK = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'

# Bandeiras
FLAG_BR = ('<svg class="flag" width="28" height="20" viewBox="0 0 28 20" aria-hidden="true">'
           '<rect width="28" height="20" fill="#009C3B"/><path d="M14 2.4 25.6 10 14 17.6 2.4 10z" fill="#FFDF00"/>'
           '<circle cx="14" cy="10" r="4.6" fill="#002776"/><path d="M9.6 9.1c2.9-.5 6.2.1 8.8 1.6" stroke="#fff" stroke-width=".9" fill="none"/></svg>')
_h = 20 / 13
_stripes = ''.join(f'<rect y="{i * _h:.3f}" width="28" height="{_h:.3f}" fill="#B22234"/>' for i in range(0, 13, 2))
_stars = ''.join(f'<circle cx="{1.4 + c * 2.2 + (r % 2) * 1.1:.2f}" cy="{1.2 + r * 1.75:.2f}" r=".45" fill="#fff"/>'
                 for r in range(6) for c in range(5 - (r % 2)))
FLAG_US = (f'<svg class="flag" width="28" height="20" viewBox="0 0 28 20" aria-hidden="true">'
           f'<rect width="28" height="20" fill="#fff"/>{_stripes}<rect width="11.2" height="{7 * _h:.3f}" fill="#3C3B6E"/>{_stars}</svg>')

FAV = "data:image/svg+xml," + quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#1D5C46"/><text x="16" y="22" font-family="Arial" font-weight="700" font-size="17" fill="#fff" text-anchor="middle">G</text></svg>')

N = len(P)

def lines(text):
    # One sentence per line: split after '. ' and wrap each sentence in a block span.
    import re
    parts = [x for x in re.split(r'(?<=[.!?])\s+', text) if x]
    return ''.join(f'<span class="line">{x}</span>' for x in parts)


def vpill(p, t, R=''):
    # Local file in videos/<id>.mp4 plays inside the site; otherwise fall back to the Drive folder.
    if os.path.exists(os.path.join(ROOT, 'videos', p['id'] + '.mp4')):
        return f'<button type="button" class="media-pill video-open" data-video="{R}videos/{p["id"]}.mp4">{PLAY}{t["video_btn"]}</button>'
    return f'<a class="media-pill" href="{p["v"]}" target="_blank" rel="noopener">{PLAY}{t["video_btn"]}</a>'


def render(lang):
    t = T[lang]
    R = '' if lang == 'pt' else '../'   # prefixo para arquivos
    MIN = money(min(p['rent'] for p in P), lang, cents=False)
    fmt = dict(N=N, MIN=MIN, DATE=ATUALIZADO[lang])
    def tx(key): return t[key].format(**fmt)
    general = wa(t['wa_general'])
    broker = wa(t['wa_broker'])
    walink = f'<a href="{general}" target="_blank" rel="noopener">WhatsApp</a>'
    mailhref = f'mailto:{EMAIL}?subject=' + quote(t['mail_subj'])
    maillink = f'<a href="{mailhref}" target="_blank" rel="noopener">{EMAIL}</a>'

    cards = []
    for p in P:
        total = p['rent'] + p['condo'] + p['iptu']
        msg = wa(t['wa_unit'].format(name=p['name'], price=money(p['rent'], lang, cents=False)))
        perks = ''.join(f'<li>{x}</li>' for x in p['perks'][lang])
        alts = p['gal'][lang]; n = len(alts)
        slides = ''.join(
            f'<picture class="slide"><source srcset="{R}images/g/{p["id"]}-{i + 1}.webp" type="image/webp">'
            f'<img src="{R}images/g/{p["id"]}-{i + 1}.jpg" alt="{p["name"]}: {a}" loading="lazy" decoding="async" width="760" height="570"></picture>'
            for i, a in enumerate(alts))
        cards.append(f'''    <article class="card reveal" id="{p['id']}" data-beds="{p['beds']}" data-rent="{p['rent']}">
      <div class="card-media gallery">
        <div class="gallery-track" tabindex="0" aria-label="{t['photos_of'].format(name=p['name'])}">{slides}</div>
        <span class="tag">{p['tag'][lang]}</span>
        {vpill(p, t, R)}
        <span class="gallery-count" aria-hidden="true">1 / {n}</span>
        <button class="gallery-btn prev" type="button" aria-label="{t['prev']}">‹</button>
        <button class="gallery-btn next" type="button" aria-label="{t['next']}">›</button>
      </div>
      <div class="card-body">
        <div>
          <h3>{p['name']}</h3>
          <p class="meta">{p['meta'][lang]}</p>
        </div>
        <ul class="perks">{perks}</ul>
        <div class="price">
          <p class="price-value">{money(p['rent'], lang, cents=False)}<span>{t['per_month']}</span></p>
          <p class="price-extra">{t['total_with'].format(v=money(total, lang))}</p>
        </div>
        <a class="btn btn-primary btn-block" href="{msg}" target="_blank" rel="noopener">{wai()}{t['visit_this']}</a>
        <div class="card-actions2">
          <button type="button" class="btn btn-outline detail-open" data-dialog="d-{p['id']}">{CAM}{t['l_desc']}</button>
          <button type="button" class="btn btn-outline share-btn" data-id="{p['id']}" data-text="{t['share_txt'].format(name=p['name'], tag=p['tag'][lang], rent=money(p['rent'], lang, cents=False))}" aria-label="{t['share']}: {p['name']}">{SHARE}</button>
        </div>
      </div>
    </article>''')
    CARDS = '\n\n'.join(cards)

    dialogs = []
    for p in P:
        d = DET[p['id']][lang]
        total = p['rent'] + p['condo'] + p['iptu']
        msg = wa(t['wa_unit'].format(name=p['name'], price=money(p['rent'], lang, cents=False)))
        ph = PHOTOS.get(p['id'])
        if ph:
            n = len(ph)
            alts = [t['photo_n'].format(i=i + 1, n=n) for i in range(n)]
            slides = ''.join(
                f'<div class="slide"><img src="{R}images/u/{p["id"]}/{i + 1:02d}.webp" alt="{p["name"]}, {alts[i]}" loading="lazy" decoding="async" width="{w}" height="{h}"></div>'
                for i, (w, h) in enumerate(ph))
            thumb_src = lambda i, pid=p['id']: f'{R}images/u/{pid}/t{i + 1:02d}.webp'
        else:
            alts = p['gal'][lang]; n = len(alts)
            slides = ''.join(
                f'<picture class="slide"><source srcset="{R}images/g/{p["id"]}-{i + 1}.webp" type="image/webp">'
                f'<img src="{R}images/g/{p["id"]}-{i + 1}.jpg" alt="{p["name"]}: {a}" loading="lazy" decoding="async" width="760" height="570"></picture>'
                for i, a in enumerate(alts))
            thumb_src = lambda i, pid=p['id']: f'{R}images/g/{pid}-{i + 1}.webp'
        groups = ''.join(f'<div class="dg"><h4>{g}</h4><ul class="checks">' + ''.join(f'<li>{CHECK}{x}</li>' for x in items) + '</ul></div>' for g, items in d['groups'])
        amen = ''.join(f'<li>{x}</li>' for x in d['amen'])
        thumbs = ''.join(f'<button type="button" class="thumb{" on" if i == 0 else ""}" data-i="{i}" aria-label="{a}"><img src="{thumb_src(i)}" alt="" loading="lazy" width="96" height="72"></button>' for i, a in enumerate(alts))
        dialogs.append(f'''<dialog class="detail" id="d-{p['id']}" aria-labelledby="dt-{p['id']}">
  <div class="detail-inner">
    <button type="button" class="detail-close" aria-label="{t['d_close']}">×</button>
    <div class="detail-media">
    <div class="card-media gallery detail-gallery">
      <div class="gallery-track" tabindex="0" aria-label="{t['photos_of'].format(name=p['name'])}">{slides}</div>
      <span class="tag">{p['tag'][lang]}</span>
      {vpill(p, t, R)}
      <button type="button" class="fs-btn" aria-label="{t['fullscreen']}" title="{t['fullscreen']}">{EXPAND}</button>
      <span class="gallery-count" aria-hidden="true">1 / {n}</span>
      <button class="gallery-btn prev" type="button" aria-label="{t['prev']}">‹</button>
      <button class="gallery-btn next" type="button" aria-label="{t['next']}">›</button>
    </div>
    <div class="thumbs">{thumbs}</div>
    </div>
    <div class="detail-body">
      <div class="detail-top"><p class="eyebrow">{p['name']}</p><button type="button" class="share-btn share-inline" data-id="{p['id']}" data-text="{t['share_txt'].format(name=p['name'], tag=p['tag'][lang], rent=money(p['rent'], lang, cents=False))}">{SHARE}{t['share']}</button></div>
      <h2 id="dt-{p['id']}">{d['head']}</h2>
      <p class="detail-intro">{d['intro']}</p>
      <div class="detail-groups">{groups}</div>
      <div class="dg"><h4>{t['d_amen']}</h4><ul class="amen">{amen}</ul></div>
      <div class="cost">
        <h4>{t['d_costs']}</h4>
        <dl>
          <dt>{t['d_rent']}</dt><dd>{money(p['rent'], lang)}</dd>
          <dt>{t['condo']}</dt><dd>{money(p['condo'], lang)}</dd>
          <dt>{t['iptu']}</dt><dd>{money(p['iptu'], lang)}</dd>
          <dt class="cost-total">{t['total']}</dt><dd class="cost-total">{money(total, lang)}</dd>
        </dl>
      </div>
      <a class="btn btn-primary btn-block btn-lg" href="{msg}" target="_blank" rel="noopener">{wai(20)}{t['visit_this']}</a>
      <p class="detail-note">{t['d_note']}</p>
    </div>
  </div>
</dialog>''')
    DIALOGS = '\n'.join(dialogs)
    menu_apts = ''.join(f'<li><button type="button" class="drawer-apt detail-open" data-dialog="d-{p["id"]}"><img src="{R}images/g/{p["id"]}-1.webp" alt="" width="64" height="48" loading="lazy"><span><strong>{p["name"]}</strong><small>{p["tag"][lang]} · {money(p["rent"], lang, cents=False)}</small></span></button></li>' for p in P)

    dep_html = ''
    if DEPOIMENTOS:
        STAR = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>'
        items = ''.join(f'''<figure class="quote reveal">
        <div class="stars" role="img" aria-label="5/5">{STAR * 5}</div>
        <blockquote>“{d["texto"][lang]}”</blockquote>
        <figcaption><span class="avatar" aria-hidden="true">{d["nome"][0]}</span><span><strong>{d["nome"]}</strong><small>{(d["cidade"] + " · ") if d["cidade"] else ""}{d["data"][lang]}</small></span></figcaption>
      </figure>''' for d in DEPOIMENTOS)
        more = f'<a class="quotes-more" href="{AIRBNB_URL[lang]}" target="_blank" rel="noopener">{t["quotes_more"]} →</a>' if AIRBNB_URL else ''
        tr = f'<p class="quotes-tr">{t["quotes_tr"]}</p>' if t['quotes_tr'] else ''
        dep_html = f'''<section id="avaliacoes" class="quotes-band">
  <div class="wrap quotes-section">
    <div class="quotes-head"><div class="section-head"><p class="eyebrow eyebrow-gold">Airbnb · Global Flats</p><h2>{t["quotes_h"]}</h2></div>{more}</div>
    <div class="quotes">{items}</div>
    {tr}
    <div class="host-card reveal"><p class="host-h">{t["host_h"]}</p><ul>{''.join(f'<li>{CHECK}{x}</li>' for x in t["host_items"])}</ul></div>
  </div>
</section>'''
    att_html = ''
    if ATENDENTE:
        foto = f'<img src="{R}{ATENDENTE["foto"]}" alt="{ATENDENTE["nome"]}" width="56" height="56">' if ATENDENTE.get('foto') else ''
        att_html = f'<div class="agent">{foto}<span>{t["agent"]} <strong>{ATENDENTE["nome"]}</strong></span></div>'

    ab_logo = f'<svg class="logo airbnb" width="40" height="40" viewBox="0 0 24 24" aria-hidden="true"><path d="{AB_SVG}"/></svg>'
    ab_cta = (f'<a class="btn btn-ab" href="{AIRBNB_URL[lang]}" target="_blank" rel="noopener">{t["ab_btn"]}</a>' if AIRBNB_URL
              else f'<p class="ab-search">{t["ab_search"]}</p>')
    AB_BAND = f'''<section class="ab-band" aria-label="Airbnb">
  <div class="wrap ab-inner reveal">
    <div class="ab-mark">{ab_logo}</div>
    <div class="ab-text"><h2>{t["ab_h"]}</h2><p>{t["ab_p"]}</p></div>
    {ab_cta}
  </div>
</section>'''
    airbnb = f'<a href="{AIRBNB_URL[lang]}" target="_blank" rel="noopener">{t["airbnb"]}</a>' if AIRBNB_URL else t['airbnb']
    faq_items = [(q, a.format(WALINK=walink, MAILLINK=maillink)) for q, a in t['faq']]
    faq_html = ''.join(f'''
      <details>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>''' for q, a in faq_items)

    steps = ''.join(f'''
    <li>
      <span class="step-n">{i + 1}</span>
      <h3>{h}</h3>
      <p>{b}</p>
    </li>''' for i, (h, b) in enumerate(t['steps']))
    proof = ''.join(f'<li>{CHECK}{x}</li>' for x in t['proof'])
    cmp_a = ''.join(f'<li>{x}</li>' for x in t['cmp_a_list'])
    cmp_b = ''.join(f'<li>{x}</li>' for x in t['cmp_b_list'])
    chips = ''.join(f'<li>{x}</li>' for x in t['brk_chips'])
    nav = t['nav']
    stats = ''.join(f'<div class="stat"><strong>{a.format(**fmt)}</strong><span>{b}</span></div>' for a, b in t['stats'])
    fvals = ['all', '0', '2', '3']
    filters = ''.join(f'<button type="button" class="chip{" on" if v == "all" else ""}" data-f="{v}" aria-pressed="{"true" if v == "all" else "false"}">{lab}</button>' for v, lab in zip(fvals, t['filters']) if v == 'all' or any(str(p['beds']) == v for p in P))
    amen_tiles = ''.join(f'<figure class="amen-tile reveal"><picture><source srcset="{R}images/g/{im}.webp" type="image/webp"><img src="{R}images/g/{im}.jpg" alt="{cap} · {where}" loading="lazy" width="760" height="570"></picture><figcaption><strong>{cap}</strong><span>{where}</span></figcaption></figure>' for im, cap, where in t['amen_tiles'])

    url = SITE + ('/' if lang == 'pt' else '/en/')
    pt_href = R + 'index.html' if lang == 'en' else '#topo'
    en_href = 'en/index.html' if lang == 'pt' else '#topo'
    lang_switch = f'''<div class="lang" role="group" aria-label="{t['lang_label']}">
      <a href="{pt_href}" hreflang="pt-BR" lang="pt-BR" title="Português" aria-label="Português"{' aria-current="true"' if lang == 'pt' else ''}>{FLAG_BR}</a>
      <a href="{en_href}" hreflang="en" lang="en" title="English" aria-label="English"{' aria-current="true"' if lang == 'en' else ''}>{FLAG_US}</a>
    </div>'''

    LD = {"@context": "https://schema.org", "@type": "ItemList", "name": t['list_name'], "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "item": {"@type": "Offer", "name": f"{p['name']} · {p['tag'][lang]}", "priceCurrency": "BRL",
         "price": f"{p['rent']:.2f}", "availability": "https://schema.org/InStock",
         "seller": {"@type": "Organization", "name": "Global Consultancy Partners Ltda", "url": SITE, "email": EMAIL, "taxID": CNPJ}}}
        for i, p in enumerate(P)]}
    LDJ = json.dumps(LD, ensure_ascii=False)

    return f'''<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tx('title')}</title>
<meta name="description" content="{tx('desc')}">
<meta property="og:type" content="website">
<meta property="og:title" content="{t['og_title']}">
<meta property="og:description" content="{tx('og_desc')}">
<meta property="og:locale" content="{t['og_locale']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{t['og_alt']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="pt-BR" href="{SITE}/">
<link rel="alternate" hreflang="en" href="{SITE}/en/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<link rel="icon" type="image/png" sizes="48x48" href="{R}images/favicon-48.png">
<link rel="apple-touch-icon" href="{R}images/apple-touch-icon.png">
<link rel="preload" as="image" href="{R}images/hero-sala.webp" type="image/webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&amp;family=Manrope:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="{R}styles.css">
<script type="application/ld+json">{LDJ}</script>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a href="#topo" class="brand">
      <img class="brand-logo" src="{R}images/logo.png" alt="Global Estadia" width="900" height="230">
    </a>
    <nav class="top-nav" aria-label="{t['nav_label']}"><a href="#imoveis">{nav[0]}</a><a href="#avaliacoes">{nav[2]}</a><a href="#duvidas">{nav[3]}</a></nav>
    {lang_switch}
    <a href="{general}" class="btn btn-primary btn-sm header-cta" target="_blank" rel="noopener">{wai()}{t['cta_short']}</a>
    <button type="button" class="menu-btn" aria-haspopup="dialog" aria-controls="menu">{MENU_I}<span>{t['menu']}</span></button>
  </div>
</header>

<dialog class="drawer" id="menu" aria-label="{t['menu']}">
  <div class="drawer-head">
    <img class="brand-logo" src="{R}images/logo.png" alt="Global Estadia" width="900" height="230">
    <button type="button" class="detail-close drawer-close" aria-label="{t['d_close']}">×</button>
  </div>
  <p class="drawer-label">{t['menu_apts']}</p>
  <ul class="drawer-apts">{menu_apts}</ul>
  <p class="drawer-label">{t['menu_nav']}</p>
  <nav class="drawer-nav" aria-label="{t['nav_label']}">
    <a href="#como-funciona">{nav[1]}</a>
    <a href="#avaliacoes">{nav[2]}</a>
    <a href="#duvidas">{nav[3]}</a>
    <a href="#corretores">{nav[4]}</a>
  </nav>
  <div class="drawer-foot">
    {lang_switch}
    <a href="{general}" class="btn btn-primary btn-block" target="_blank" rel="noopener">{wai()}{t['cta_long']}</a>
    <a class="drawer-mail" href="{mailhref}" target="_blank" rel="noopener">{EMAIL}</a>
  </div>
</dialog>

<main>

<section id="topo" class="hero-wrap">
  <div class="wrap hero">
  <div class="hero-text">
    <p class="eyebrow eyebrow-gold">{t['eyebrow']}</p>
    <h1>{lines(t['h1'])}</h1>
    <p class="lead">{lines(tx('lead'))}</p>
    <div class="hero-actions">
      <a href="{general}" class="btn btn-primary btn-lg" target="_blank" rel="noopener">{wai(20)}{t['cta_long']}</a>
      <a href="#imoveis" class="btn btn-ghost btn-lg">{tx('see_all')}</a>
    </div>
    {att_html}
    <ul class="proof-row">{proof}</ul>
  </div>
  <div class="hero-collage">
    <picture class="hc-main"><source srcset="{R}images/hero-sala.webp" type="image/webp"><img src="{R}images/hero-sala.jpg" alt="{t['hero_alt']}" width="908" height="1210" fetchpriority="high"></picture>
    <picture class="hc-a"><source srcset="{R}images/g/spettacolo-42-3.webp" type="image/webp"><img src="{R}images/g/spettacolo-42-3.jpg" alt="{PID['spettacolo-42']['name']}: {PID['spettacolo-42']['gal'][lang][2]}" width="760" height="570"></picture>
    <picture class="hc-b"><source srcset="{R}images/g/esplanada-102-3.webp" type="image/webp"><img src="{R}images/g/esplanada-102-3.jpg" alt="{PID['esplanada-102']['name']}: {PID['esplanada-102']['gal'][lang][2]}" width="760" height="570"></picture>
    <div class="hero-badge">
      <span class="hero-count">{N}</span>
      <div>
        <strong>{t['badge']}</strong>
        <span>{tx('updated')}</span>
      </div>
    </div>
  </div>
  </div>
</section>

<section id="imoveis" class="band">
  <div class="wrap listings">
    <div class="list-top">
      <div class="section-head">
        <p class="eyebrow">{t['list_eyebrow']}</p>
        <h2>{t['list_h']}</h2>
        <p>{t['list_p']}</p>
      </div>
      <div class="filters" role="group" aria-label="Filtro">
        <div class="chipset">{filters}</div>
        <label class="sort">{t['sort_label']}
          <select id="sort"><option value="desc">{t['sort_opts'][0]}</option><option value="asc">{t['sort_opts'][1]}</option></select>
        </label>
      </div>
    </div>
    <div class="grid" id="grid">
{CARDS}
    </div>
  </div>
</section>

<section id="lazer" class="amen-section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow eyebrow-gold">{t['amen_eyebrow']}</p>
      <h2>{t['amen_h']}</h2>
      <p>{t['amen_p']}</p>
    </div>
    <div class="amen-grid">{amen_tiles}</div>
  </div>
</section>

<section id="como-funciona" class="wrap steps-section">
  <div class="section-head">
    <h2>{t['steps_h']}</h2>
  </div>
  <ol class="steps reveal">{steps}
  </ol>
  <div class="compare">
    <div class="compare-col">
      <h3>{t['cmp_a']}</h3>
      <ul>{cmp_a}</ul>
    </div>
    <div class="compare-col compare-win">
      <h3>{t['cmp_b']}</h3>
      <ul>{cmp_b}</ul>
    </div>
  </div>
</section>

{dep_html}

<section id="duvidas" class="band">
  <div class="wrap faq-section">
    <div class="section-head">
      <h2>{t['faq_h']}</h2>
    </div>
    <div class="faq">{faq_html}
    </div>
  </div>
</section>

<section id="corretores" class="dark">
  <div class="wrap brokers">
    <div class="brokers-text">
      <p class="eyebrow eyebrow-gold">{t['brk_eyebrow']}</p>
      <h2>{t['brk_h']}</h2>
      <p>{t['brk_p']}</p>
    </div>
    <div class="notice">
      <h3>{t['brk_box']}</h3>
      <p>{t['brk_send']}</p>
      <ul class="chips">{chips}</ul>
      <a href="{broker}" class="btn btn-primary btn-block" target="_blank" rel="noopener">{wai()}{t['brk_btn']}</a>
      <p class="small">{t['brk_small']}</p>
    </div>
  </div>
</section>

{AB_BAND}
<section id="contato" class="cta-band">
  <picture class="cta-bg"><source srcset="{R}images/cta-bg.webp" type="image/webp"><img src="{R}images/cta-bg.jpg" alt="" loading="lazy" width="1600" height="840"></picture>
  <div class="wrap contact reveal">
    <h2>{lines(t['end_h'])}</h2>
    <p>{t['end_p']}</p>
    <a href="{general}" class="btn btn-primary btn-xl" target="_blank" rel="noopener">{wai(20)}{t['cta_long']}</a>
  </div>
</section>

</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-id">
      <img class="footer-logo" src="{R}images/logo-white.png" alt="Global Estadia" width="900" height="230" loading="lazy">
      <span class="brand-name">Global Consultancy Partners Ltda</span>
      <span>CNPJ {CNPJ}</span>
    </div>
    <div class="footer-id footer-right">
      <span>{t['foot_tag']}</span>
      <a class="footer-wa" href="{general}" target="_blank" rel="noopener">{wai(18)}{t['foot_wa']}</a>
      <a href="{mailhref}" target="_blank" rel="noopener">{EMAIL}</a>
    </div>
  </div>
</footer>

{DIALOGS}
<dialog class="share-sheet" id="share" aria-labelledby="share-h">
  <button class="detail-close" type="button" aria-label="{t['d_close']}">✕</button>
  <p class="share-h" id="share-h">{t['share_h']}</p>
  <p class="share-name"></p>
  <div class="share-opts">
    <a class="share-opt share-wa" href="#" target="_blank" rel="noopener">{wai(20)}WhatsApp</a>
    <button type="button" class="share-opt share-copy"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>{t['share_copy']}</button>
    <a class="share-opt share-mail" href="#" target="_blank" rel="noopener"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>{t['share_mail']}</a>
  </div>
  <input class="share-url" type="text" readonly aria-label="Link">
</dialog>
<dialog class="vid" id="vid" aria-label="{t['l_video']}">
  <button class="detail-close" type="button" aria-label="{t['d_close']}">✕</button>
  <video controls playsinline preload="none"></video>
</dialog>

<a href="{general}" class="mobile-cta" target="_blank" rel="noopener">{wai(20)}{t['cta_short']}</a>

<script>
document.querySelectorAll('.gallery').forEach(function (g) {{
  var t = g.querySelector('.gallery-track'), c = g.querySelector('.gallery-count'), n = t.children.length;
  if (n < 2) {{ g.classList.add('single'); return; }}
  function idx() {{ var w = t.clientWidth; if (!w) return 0; return Math.min(n - 1, Math.max(0, Math.round(t.scrollLeft / w))); }}
  function go(d) {{ t.scrollTo({{ left: ((idx() + d + n) % n) * t.clientWidth, behavior: 'smooth' }}); }}
  g.querySelector('.prev').addEventListener('click', function () {{ go(-1); }});
  g.querySelector('.next').addEventListener('click', function () {{ go(1); }});
  t.addEventListener('scroll', function () {{ if (t.clientWidth) c.textContent = (idx() + 1) + ' / ' + n; }}, {{ passive: true }});
  t.addEventListener('keydown', function (e) {{ if (e.key === 'ArrowRight') {{ e.preventDefault(); go(1); }} if (e.key === 'ArrowLeft') {{ e.preventDefault(); go(-1); }} }});
}});
var menu = document.getElementById('menu');
document.querySelector('.menu-btn').addEventListener('click', function () {{ if (menu.showModal) {{ menu.showModal(); document.body.classList.add('modal-open'); }} }});
menu.querySelectorAll('.drawer-nav a').forEach(function (a) {{ a.addEventListener('click', function () {{ menu.close(); }}); }});
document.querySelectorAll('.detail-open').forEach(function (b) {{
  b.addEventListener('click', function () {{
    var d = document.getElementById(b.dataset.dialog);
    if (menu.open) menu.close();
    if (d && d.showModal) {{ d.showModal(); document.body.classList.add('modal-open'); d.querySelector('.gallery-track').scrollLeft = 0; }}
  }});
}});
document.querySelectorAll('dialog.detail').forEach(function (d) {{
  var t = d.querySelector('.gallery-track'), th = d.querySelectorAll('.thumb');
  th.forEach(function (b) {{ b.addEventListener('click', function () {{ t.scrollTo({{ left: +b.dataset.i * t.clientWidth, behavior: 'smooth' }}); }}); }});
  var row = th.length ? th[0].parentElement : null, last = -1;
  t.addEventListener('scroll', function () {{ if (!t.clientWidth) return; var i = Math.round(t.scrollLeft / t.clientWidth); if (i === last) return; last = i;
    th.forEach(function (b, k) {{ b.classList.toggle('on', k === i); }});
    var b = th[i]; if (row && b) row.scrollTo({{ left: b.offsetLeft - row.offsetLeft - (row.clientWidth - b.offsetWidth) / 2, behavior: 'smooth' }});
  }}, {{ passive: true }});
  var fs = d.querySelector('.fs-btn'), g = d.querySelector('.detail-gallery');
  fs.addEventListener('click', function () {{
    try {{ if (document.fullscreenElement) document.exitFullscreen(); else if (g.requestFullscreen) g.requestFullscreen().catch(function () {{ g.classList.toggle('big'); }}); else g.classList.toggle('big'); }} catch (e) {{ g.classList.toggle('big'); }}
  }});
}});
var toast = document.createElement('div'); toast.className = 'toast'; toast.setAttribute('role', 'status'); document.body.appendChild(toast);
function showToast(m) {{ (document.querySelector('dialog[open]') || document.body).appendChild(toast); toast.textContent = m; toast.classList.add('on'); clearTimeout(showToast.t); showToast.t = setTimeout(function () {{ toast.classList.remove('on'); }}, 2200); }}
document.querySelectorAll('a[href^="mailto:{EMAIL}"]').forEach(function (a) {{ a.addEventListener('click', function () {{
  var done = function () {{ showToast('{t['mail_ok']}{EMAIL}'); }};
  if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText('{EMAIL}').then(done, function () {{}});
}}); }});
var sheet = document.getElementById('share'), surl = sheet.querySelector('.share-url');
var canon = (document.querySelector('link[rel=canonical]') || {{}}).href || location.href.split('#')[0];
function copyLink() {{
  var ok = function () {{ showToast('{t['share_ok']}'); }};
  surl.focus(); surl.select();
  try {{ if (document.execCommand('copy')) {{ ok(); return; }} }} catch (e) {{}}
  if (navigator.clipboard) navigator.clipboard.writeText(surl.value).then(ok, function () {{}});
}}
sheet.querySelector('.share-copy').addEventListener('click', copyLink);
function openSheet(url, text, name) {{
  surl.value = url; sheet.querySelector('.share-name').textContent = name;
  sheet.querySelector('.share-wa').href = 'https://wa.me/?text=' + encodeURIComponent(text + ' ' + url);
  sheet.querySelector('.share-mail').href = 'mailto:?subject=' + encodeURIComponent(name) + '&body=' + encodeURIComponent(text + '\\n' + url);
  sheet.showModal(); document.body.classList.add('modal-open');
}}
document.querySelectorAll('.share-btn').forEach(function (b) {{ b.addEventListener('click', function () {{
  var url = canon + '#' + b.dataset.id, text = b.dataset.text, name = text.split(' · ')[0];
  var framed = false; try {{ framed = window.self !== window.top; }} catch (e) {{ framed = true; }}
  if (navigator.share && !framed && window.matchMedia('(hover: none)').matches) {{
    navigator.share({{ title: name, text: text, url: url }}).catch(function (e) {{ if (!e || e.name !== 'AbortError') openSheet(url, text, name); }});
  }} else openSheet(url, text, name);
}}); }});
function openFromHash() {{
  var id = location.hash.slice(1), d = id && document.getElementById('d-' + id);
  if (d && d.showModal && !d.open) {{ var c = document.getElementById(id); if (c) c.scrollIntoView(); d.showModal(); document.body.classList.add('modal-open'); }}
}}
window.addEventListener('hashchange', openFromHash);
var vd = document.getElementById('vid');
document.querySelectorAll('.video-open').forEach(function (b) {{ b.addEventListener('click', function () {{
  var v = vd.querySelector('video'); v.src = b.dataset.video; vd.showModal(); document.body.classList.add('modal-open'); v.play().catch(function () {{}});
}}); }});
vd.addEventListener('close', function () {{ var v = vd.querySelector('video'); v.pause(); v.removeAttribute('src'); v.load(); }});
document.querySelectorAll('.detail-open[data-fs]').forEach(function (b) {{ b.addEventListener('click', function () {{
  var d = document.getElementById(b.dataset.dialog), g = d && d.querySelector('.detail-gallery'); if (g && window.matchMedia('(min-width: 900px)').matches) g.scrollIntoView({{ block: 'nearest' }});
}}); }});
document.querySelectorAll('dialog').forEach(function (d) {{
  var c = d.querySelector('.detail-close'); if (c) c.addEventListener('click', function () {{ d.close(); }});
  d.addEventListener('click', function (e) {{ if (e.target === d) d.close(); }});
  d.addEventListener('close', function () {{ if (!document.querySelector('dialog[open]')) document.body.classList.remove('modal-open'); }});
}});
(function () {{
  var grid = document.getElementById('grid'); if (!grid) return;
  var chips = document.querySelectorAll('.chip'), sel = document.getElementById('sort');
  chips.forEach(function (c) {{ c.addEventListener('click', function () {{
    chips.forEach(function (x) {{ x.classList.toggle('on', x === c); x.setAttribute('aria-pressed', x === c ? 'true' : 'false'); }});
    grid.querySelectorAll('.card').forEach(function (card) {{ card.hidden = !(c.dataset.f === 'all' || card.dataset.beds === c.dataset.f); }});
  }}); }});
  sel.addEventListener('change', function () {{
    var cards = Array.prototype.slice.call(grid.querySelectorAll('.card'));
    cards.sort(function (a, b) {{ return sel.value === 'asc' ? a.dataset.rent - b.dataset.rent : b.dataset.rent - a.dataset.rent; }});
    cards.forEach(function (c) {{ grid.appendChild(c); }});
  }});
}})();
(function () {{
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {{ els.forEach(function (e) {{ e.classList.add('in'); }}); return; }}
  document.documentElement.classList.add('js-reveal');
  var io = new IntersectionObserver(function (es) {{ es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}); }}, {{ rootMargin: '0px 0px -8% 0px' }});
  els.forEach(function (e) {{ io.observe(e); }});
}})();
(function () {{
  var cta = document.querySelector('.mobile-cta'), hero = document.querySelector('.hero-actions');
  if (!cta || !hero || !('IntersectionObserver' in window)) {{ if (cta) cta.classList.add('show'); return; }}
  new IntersectionObserver(function (e) {{ cta.classList.toggle('show', !e[0].isIntersecting); }}).observe(hero);
}})();
document.querySelectorAll('dialog.detail').forEach(function (d) {{ d.addEventListener('close', function () {{ if (location.hash === '#' + d.id.slice(2) && history.replaceState) history.replaceState(null, '', location.pathname + location.search); }}); }});
openFromHash();
</script>
</body>
</html>
'''

if __name__ == '__main__':
    open('index.html', 'w', encoding='utf-8').write(render('pt'))
    os.makedirs('en', exist_ok=True)
    open('en/index.html', 'w', encoding='utf-8').write(render('en'))
    for p in P:
        print(p['name'], money(p['rent'] + p['condo'] + p['iptu'], 'pt'))
