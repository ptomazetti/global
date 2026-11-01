"""Gera index.html (portugues) e en/index.html (ingles).
Rode a partir da raiz do repositorio:  python3 tools/build.py
"""
from urllib.parse import quote
import json, os

# ===== CONFIGURACAO: edite aqui =====================================
SITE = 'https://globalestadia.com.br'
EMAIL = 'contato@globalestadia.com.br'
WA = '5515997470301'
WA_SHOW = '+55 (15) 99747-0301'
CNPJ = '50.945.139/0001-86'
ATUALIZADO = {'pt': '1 de novembro de 2026', 'en': '1 November 2026'}  # mude sempre que um imovel entrar ou sair
AIRBNB_URL = ''   # link do perfil Global Flats no Airbnb
ATENDENTE = {}    # ex.: {'nome': 'Paula', 'foto': 'images/paula.jpg'}
DEPOIMENTOS = []  # ex.: [{'texto': {'pt': '...', 'en': '...'}, 'nome': 'Ana', 'imovel': 'Alpha Club'}]
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
 dict(id='spettacolo-42', name='Spettacolo Patriani', rent=3490, condo=615.09, iptu=56.30,
  tag={'pt': 'Studio alto padrão', 'en': 'Premium studio'},
  meta={'pt': 'Apto. 42 · 76 m² de área total', 'en': 'Apt. 42 · 76 m² total area'},
  perks={'pt': ['2 garagens cobertas e depósito de 10 m²', 'Varanda panorâmica, cama box Queen', 'Piscina com raia, SPA, sauna e academia'],
         'en': ['2 covered parking spaces and 10 m² storage', 'Panoramic balcony, Queen bed', 'Lap pool, spa, sauna and gym']},
  gal={'pt': ['Sala com vista pela varanda panorâmica', 'Sala de estar com sofá e poltronas', 'Cozinha com armários planejados e cooktop', 'SPA com hidromassagem do condomínio', 'Fachada do Spettacolo Patriani'],
       'en': ['Living room with panoramic balcony view', 'Living room with sofa and armchairs', 'Kitchen with built-in cabinets and cooktop', 'Building spa with hot tub', 'Spettacolo Patriani entrance']},
  f='https://drive.google.com/drive/folders/1q39K2Jp_P_wErO56gb_jWGZT09iCpRCm?usp=sharing',
  v='https://drive.google.com/drive/folders/1lPg1uhrh6_9gQgG7jaKDxVGTWJAIPtrx?usp=drive_link',
  d='https://drive.google.com/file/d/1akjtOVeacGJNRz2Ihp5uc-KQfwCBWlxQ/view?usp=drive_link'),
 dict(id='alpha-club-j42', name='Alpha Club J42', rent=2890, condo=464.19, iptu=158.00,
  tag={'pt': '2 dormitórios c/ suíte', 'en': '2 bedrooms, 1 en suite'},
  meta={'pt': 'Apto. 42 · Bloco J · Campolim', 'en': 'Apt. 42 · Block J · Campolim'},
  perks={'pt': ['Ar-condicionado 12.000 BTUs na suíte', 'Cama box Queen, Smart TV, cortina blackout', 'Varanda gourmet, condomínio clube'],
         'en': ['12,000 BTU air conditioning in the master bedroom', 'Queen bed, Smart TV, blackout curtains', 'Barbecue balcony, club-style complex']},
  gal={'pt': ['Sala com bar iluminado e bancada', 'Cozinha com geladeira, fogão e micro-ondas'],
       'en': ['Living room with lit bar and counter', 'Kitchen with fridge, stove and microwave']},
  f='https://drive.google.com/drive/folders/1bPidYHmKlhAE6bBfmmKMkpROLZA144Wz?usp=drive_link',
  v='https://drive.google.com/drive/folders/1Aj7hwWm6NFKFlbf-Cg_wN6XHlmL7M8kM?usp=drive_link',
  d='https://drive.google.com/file/d/1W3QlSmMlkzd-SnY9_mjDsCZN_WANdPRY/view?usp=sharing'),
 dict(id='esplanada-102', name='Residencial Esplanada', rent=2890, condo=500.00, iptu=105.33,
  tag={'pt': '3 dormitórios', 'en': '3 bedrooms'},
  meta={'pt': 'Apto. 102 · Bloco 2', 'en': 'Apt. 102 · Block 2'},
  perks={'pt': ['Cozinha equipada, geladeira 440 L, cooktop e forno', 'Máquina lava e seca, ar-condicionado na sala', '1 vaga, condomínio clube'],
         'en': ['Equipped kitchen, 440 L fridge, cooktop and oven', 'Washer-dryer, air conditioning in the living room', '1 parking space, club-style complex']},
  gal={'pt': ['Sala integrada com mesa de jantar', 'Cozinha com geladeira e micro-ondas', 'Dormitório com armário planejado'],
       'en': ['Open-plan living and dining room', 'Kitchen with fridge and microwave', 'Bedroom with built-in wardrobe']},
  f='https://drive.google.com/drive/folders/1A19Eb5ZPVLWmBcxqc6R4a2GPwvbjgVFB?usp=drive_link',
  v='https://drive.google.com/drive/folders/19i1YFcf9KCxrye3UG8FQDM-IXv_1g_qE?usp=drive_link',
  d='https://drive.google.com/file/d/19NxWZqBZ20AZ7AQVyDnz_o85rwfdnqPo/view?usp=sharing'),
 dict(id='alpha-club-i41', name='Alpha Club I41', rent=2790, condo=497.77, iptu=158.12,
  tag={'pt': '2 dormitórios c/ suíte', 'en': '2 bedrooms, 1 en suite'},
  meta={'pt': 'Apto. 41 · Bloco I · Campolim', 'en': 'Apt. 41 · Block I · Campolim'},
  perks={'pt': ['Dois quartos com cama box de casal', 'Mesa de jantar para 4 lugares', 'Varanda gourmet, 1 vaga, condomínio clube'],
         'en': ['Two bedrooms with double beds', 'Dining table for 4', 'Barbecue balcony, 1 parking space, club-style complex']},
  gal={'pt': ['Sala com sofá e Smart TV', 'Cozinha equipada com máquina de lavar', 'Academia do condomínio', 'Piscina do condomínio'],
       'en': ['Living room with sofa and Smart TV', 'Equipped kitchen with washing machine', 'Building gym', 'Building pool']},
  f='https://drive.google.com/drive/folders/1UxoTaZttGauF5RwCaPovwjylUFDpiMxK?usp=drive_link',
  v='https://drive.google.com/drive/folders/1ZqcbXnrIE4xuA2ob8gaRtECV8nynp88b?usp=drive_link',
  d='https://drive.google.com/file/d/1PBosWcqSD6zJ6Efxw_TIPX-IsAMZ3zzL/view?usp=drive_link'),
 dict(id='vida-plena-c65', name='Vida Plena C65', rent=2790, condo=406.42, iptu=61.84,
  tag={'pt': '2 dormitórios', 'en': '2 bedrooms'},
  meta={'pt': 'Apto. 65 · Bloco C · Campolim', 'en': 'Apt. 65 · Block C · Campolim'},
  perks={'pt': ['Armários planejados em todos os cômodos', 'Bancada para home office, iluminação LED', 'Condomínio com lazer completo'],
         'en': ['Built-in cabinets in every room', 'Home office desk, LED lighting', 'Full leisure facilities']},
  gal={'pt': ['Sala com mesa de jantar', 'Cozinha com geladeira, fogão e micro-ondas', 'Dormitório com cama box e armário'],
       'en': ['Living room with dining table', 'Kitchen with fridge, stove and microwave', 'Bedroom with bed and wardrobe']},
  f='https://drive.google.com/drive/folders/1qV2qAFvA47z2pMG8QX_9GhA8e6oTtLZb?usp=drive_link',
  v='https://drive.google.com/drive/folders/1PODn9-X7koK7EUwgue70c9oIHWpFSGll?usp=drive_link',
  d='https://drive.google.com/file/d/1J17liUYRHgMADoPXDzAqgiYSOjdORVh1/view?usp=sharing'),
]

T = {
 'pt': dict(
  html_lang='pt-BR', og_locale='pt_BR',
  title='Apartamentos mobiliados em Sorocaba a partir de {MIN} | Global',
  desc='{N} apartamentos mobiliados prontos para morar em Sorocaba, de studio a 3 dormitórios. Aluguel a partir de {MIN}. Agende sua visita pelo WhatsApp.',
  og_title='Apartamentos mobiliados em Sorocaba, prontos para morar',
  og_desc='{N} apartamentos disponíveis, de studio a 3 dormitórios. Aluguel a partir de {MIN}. Agende sua visita pelo WhatsApp.',
  og_alt='Sala mobiliada de um dos apartamentos da Global',
  nav_label='Principal', nav=['Apartamentos', 'Como funciona', 'Dúvidas', 'Corretores'],
  lang_label='Idioma', cta_short='Agendar visita', cta_long='Agendar visita pelo WhatsApp',
  eyebrow='Locação mobiliada em Sorocaba',
  h1='Apartamento mobiliado. Você só traz a mala.',
  lead='{N} apartamentos prontos para morar, de studio a 3 dormitórios, em condomínios com lazer. Aluguel a partir de {MIN}. Visite antes de decidir.',
  see_all='Ver os {N} apartamentos',
  proof=['Pintado e higienizado a cada locação', '3 opções de garantia', 'Fotos, vídeo e descrição de cada imóvel'],
  hero_alt='Sala mobiliada do Spettacolo Patriani com sofá, poltronas e tapete',
  badge='disponíveis hoje', updated='Lista atualizada em {DATE}',
  agent='Quem responde no WhatsApp:',
  list_h='Escolha o seu e marque a visita',
  list_p='Valores completos à vista: aluguel, condomínio e IPTU. Sem surpresa no contrato.',
  photos_of='Fotos do {name}', prev='Foto anterior', next='Próxima foto',
  per_month=' /mês de aluguel', condo='Condomínio', iptu='IPTU', total='Total mensal',
  visit_this='Quero visitar este', l_photos='Fotos', l_video='Vídeo', l_desc='Descrição',
  steps_h='Da visita às chaves em 3 passos',
  steps=[('Escolha e visite', 'Toque em "Quero visitar este" no apartamento. A mensagem já vai pronta no WhatsApp, com o nome do imóvel.'),
         ('Escolha a garantia', 'Seguro fiança, caução de 3 aluguéis ou fiador. Você usa a que for mais simples para você.'),
         ('Entre com a mala', 'Móveis, cozinha equipada e eletrodomésticos já estão lá. O apartamento é pintado e higienizado antes de você chegar.')],
  cmp_a='Alugar um apartamento vazio', cmp_a_list=['Comprar sofá, cama, mesa e cortinas', 'Comprar geladeira, fogão, micro-ondas e máquina de lavar', 'Pagar frete, montagem e instalação', 'Semanas até a casa ficar pronta'],
  cmp_b='Alugar com a Global', cmp_b_list=['Móveis e armários planejados já instalados', 'Eletrodomésticos funcionando', 'Apartamento pintado e higienizado', 'Você muda sem esperar móveis chegarem'],
  quotes_h='Quem já mora',
  faq_h='Perguntas antes de visitar',
  faq=[('Quais garantias vocês aceitam?', 'Seguro fiança, caução de 3 aluguéis ou fiador.'),
       ('O valor do aluguel inclui condomínio e IPTU?', 'Não. Condomínio e IPTU são cobrados à parte. Cada apartamento mostra os três valores e o total mensal, para você comparar sem surpresa.'),
       ('O que exatamente vem no apartamento?', 'Cada imóvel tem uma descrição completa com a lista de móveis e eletrodomésticos. Toque em "Descrição" no card do apartamento.'),
       ('O apartamento é limpo antes de eu entrar?', 'Sim. A cada nova locação, o apartamento é pintado e higienizado.'),
       ('Como agendo uma visita?', 'Pelo WhatsApp {WALINK}. Diga qual apartamento e o melhor dia e horário para você. Se preferir, escreva para {MAILLINK}.')],
  short_q='Preciso de uma estadia curta. Vocês têm?', short_a='Sim, para estadias curtas procure por {AIRBNB}.', airbnb='Global Flats no Airbnb',
  brk_eyebrow='Para corretores parceiros', brk_h='Feche locação sem montar material.',
  brk_p='Cada apartamento já tem fotos, vídeo e descrição prontos para você enviar ao cliente. Use os links dos cards ou peça o material completo.',
  brk_box='Para agendar uma visita', brk_send='Envie em uma única mensagem:', brk_chips=['Nome', 'RG', 'CRECI', 'Imóvel', 'Dia e horário'],
  brk_btn='Enviar pedido de visita', brk_small='O botão abre o WhatsApp com esses campos já preenchidos.',
  end_h='Gostou de um? Marque a visita hoje.', end_p='Cada apartamento é único. Quando ele é alugado, sai da lista.',
  foot_tag='Locação de apartamentos mobiliados · Sorocaba',
  wa_general='Olá! Vi o site da Global e quero agendar uma visita. Meu nome é: ',
  wa_unit='Olá! Vi o site da Global e quero visitar o {name} ({price}). Meu nome é: ',
  wa_broker='Olá! Sou corretor(a) e quero agendar uma visita.\nNome:\nRG:\nCRECI:\nImóvel:\nDia e horário:',
  list_name='Apartamentos mobiliados para locação',
 ),
 'en': dict(
  html_lang='en', og_locale='en_US',
  title='Furnished apartments for rent in Sorocaba, Brazil, from {MIN} | Global',
  desc='{N} fully furnished apartments ready to move into in Sorocaba, Brazil, from studio to 3 bedrooms. Rent from {MIN} a month. Book a viewing on WhatsApp.',
  og_title='Furnished apartments in Sorocaba, ready to move in',
  og_desc='{N} apartments available, from studio to 3 bedrooms. Rent from {MIN} a month. Book a viewing on WhatsApp.',
  og_alt='Furnished living room in one of the Global apartments',
  nav_label='Main', nav=['Apartments', 'How it works', 'FAQ', 'Agents'],
  lang_label='Language', cta_short='Book a viewing', cta_long='Book a viewing on WhatsApp',
  eyebrow='Furnished rentals in Sorocaba, Brazil',
  h1='Fully furnished. Just bring your suitcase.',
  lead='{N} apartments ready to move into, from studio to 3 bedrooms, in buildings with leisure facilities. Rent from {MIN} a month. See it before you decide.',
  see_all='See all {N} apartments',
  proof=['Repainted and deep cleaned before every new tenant', '3 rental guarantee options', 'Photos, video and full description of each apartment'],
  hero_alt='Furnished living room at Spettacolo Patriani with sofa, armchairs and rug',
  badge='available today', updated='List updated {DATE}',
  agent='Your contact on WhatsApp:',
  list_h='Choose yours and book a viewing',
  list_p='Full costs shown upfront: rent, condo fee and property tax (IPTU). No surprises in the contract.',
  photos_of='Photos of {name}', prev='Previous photo', next='Next photo',
  per_month=' /month rent', condo='Condo fee', iptu='IPTU tax', total='Total per month',
  visit_this='I want to see this one', l_photos='Photos', l_video='Video', l_desc='Description',
  steps_h='From viewing to keys in 3 steps',
  steps=[('Choose and visit', 'Tap "I want to see this one" on the apartment. WhatsApp opens with your message ready, including the apartment name.'),
         ('Pick your guarantee', 'Rent guarantee insurance (seguro fiança), a deposit of 3 months’ rent (caução) or a guarantor (fiador). Use whichever is easiest for you.'),
         ('Move in with a suitcase', 'Furniture, an equipped kitchen and appliances are already there. The apartment is repainted and deep cleaned before you arrive.')],
  cmp_a='Renting an empty apartment', cmp_a_list=['Buy a sofa, bed, table and curtains', 'Buy a fridge, stove, microwave and washing machine', 'Pay for delivery, assembly and installation', 'Weeks before the place is ready'],
  cmp_b='Renting with Global', cmp_b_list=['Furniture and built-in cabinets already in place', 'Appliances working', 'Apartment repainted and deep cleaned', 'Move in without waiting for furniture'],
  quotes_h='What our tenants say',
  faq_h='Questions before your viewing',
  faq=[('Which rental guarantees do you accept?', 'Rent guarantee insurance (seguro fiança), a deposit of 3 months’ rent (caução) or a guarantor (fiador).'),
       ('Does the rent include the condo fee and IPTU tax?', 'No. The condo fee and IPTU property tax are charged separately. Each apartment shows all three amounts and the monthly total, so you can compare with no surprises.'),
       ('What exactly comes with the apartment?', 'Each apartment has a full description listing the furniture and appliances. Tap "Description" on the apartment card. The description is in Portuguese.'),
       ('Is the apartment cleaned before I move in?', 'Yes. Before every new tenant, the apartment is repainted and deep cleaned.'),
       ('How do I book a viewing?', 'On WhatsApp at {WALINK}. Tell us which apartment and the best day and time for you. You can also email {MAILLINK}.')],
  short_q='I need a short stay. Do you offer that?', short_a='Yes. For short stays, look for {AIRBNB}.', airbnb='Global Flats on Airbnb',
  brk_eyebrow='For partner real estate agents', brk_h='Close rentals without building your own material.',
  brk_p='Every apartment already has photos, video and a description ready to send to your client. Use the links on each card or ask for the full pack.',
  brk_box='To book a viewing', brk_send='Send in one message:', brk_chips=['Name', 'ID (RG)', 'CRECI', 'Apartment', 'Day and time'],
  brk_btn='Send viewing request', brk_small='The button opens WhatsApp with these fields ready to fill in.',
  end_h='Like one? Book your viewing today.', end_p='Every apartment is one of a kind. Once it is rented, it comes off the list.',
  foot_tag='Furnished apartment rentals · Sorocaba, Brazil',
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
DOC = '<svg width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>'
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

def render(lang):
    t = T[lang]
    R = '' if lang == 'pt' else '../'   # prefixo para arquivos
    MIN = money(min(p['rent'] for p in P), lang, cents=False)
    fmt = dict(N=N, MIN=MIN, DATE=ATUALIZADO[lang])
    def tx(key): return t[key].format(**fmt)
    general = wa(t['wa_general'])
    broker = wa(t['wa_broker'])
    walink = f'<a href="{general}" target="_blank" rel="noopener">{WA_SHOW}</a>'
    maillink = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

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
        cards.append(f'''    <article class="card" id="{p['id']}">
      <div class="card-media gallery">
        <div class="gallery-track" tabindex="0" aria-label="{t['photos_of'].format(name=p['name'])}">{slides}</div>
        <span class="tag">{p['tag'][lang]}</span>
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
          <p class="price-extra">{t['condo']} {money(p['condo'], lang)} · {t['iptu']} {money(p['iptu'], lang)}</p>
          <p class="price-total">{t['total']}: {money(total, lang)}</p>
        </div>
        <a class="btn btn-primary btn-block" href="{msg}" target="_blank" rel="noopener">{wai()}{t['visit_this']}</a>
        <div class="card-links">
          <a href="{p['f']}" target="_blank" rel="noopener">{CAM}{t['l_photos']}</a>
          <a href="{p['v']}" target="_blank" rel="noopener">{PLAY}{t['l_video']}</a>
          <a href="{p['d']}" target="_blank" rel="noopener">{DOC}{t['l_desc']}</a>
        </div>
      </div>
    </article>''')
    CARDS = '\n\n'.join(cards)

    dep_html = ''
    if DEPOIMENTOS:
        items = ''.join(f'<figure class="quote"><blockquote>“{d["texto"][lang]}”</blockquote><figcaption>{d["nome"]} · {d["imovel"]}</figcaption></figure>' for d in DEPOIMENTOS)
        dep_html = f'<section id="depoimentos" class="wrap quotes-section"><div class="section-head"><h2>{t["quotes_h"]}</h2></div><div class="quotes">{items}</div></section>'
    att_html = ''
    if ATENDENTE:
        foto = f'<img src="{R}{ATENDENTE["foto"]}" alt="{ATENDENTE["nome"]}" width="56" height="56">' if ATENDENTE.get('foto') else ''
        att_html = f'<div class="agent">{foto}<span>{t["agent"]} <strong>{ATENDENTE["nome"]}</strong></span></div>'

    airbnb = f'<a href="{AIRBNB_URL}" target="_blank" rel="noopener">{t["airbnb"]}</a>' if AIRBNB_URL else t['airbnb']
    faq_items = [(q, a.format(WALINK=walink, MAILLINK=maillink)) for q, a in t['faq']]
    faq_items += [(q[lang], a[lang]) for q, a in FAQ_EXTRA]
    faq_html = ''.join(f'''
      <details>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>''' for q, a in faq_items)
    faq_html += f'''
      <details>
        <summary>{t['short_q']}</summary>
        <p class="airbnb-line"><svg class="logo airbnb" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="{AB_SVG}"/></svg>{t['short_a'].format(AIRBNB=airbnb)}</p>
      </details>'''

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
         "seller": {"@type": "Organization", "name": "Global Consultancy Partners Ltda", "url": SITE, "email": EMAIL, "taxID": CNPJ, "telephone": "+" + WA}}}
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
<link rel="icon" href="{FAV}">
<link rel="preload" as="image" href="{R}images/hero-sala.webp" type="image/webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&amp;family=Manrope:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="{R}styles.css">
<script type="application/ld+json">{LDJ}</script>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a href="#topo" class="brand">
      <span class="brand-mark" aria-hidden="true">G</span>
      <span class="brand-name">Global<span class="brand-rest"> Consultancy Partners</span></span>
    </a>
    <nav aria-label="{t['nav_label']}" class="nav">
      <a href="#imoveis">{nav[0]}</a>
      <a href="#como-funciona">{nav[1]}</a>
      <a href="#duvidas">{nav[2]}</a>
      <a href="#corretores">{nav[3]}</a>
    </nav>
    {lang_switch}
    <a href="{general}" class="btn btn-primary btn-sm header-cta" target="_blank" rel="noopener">{wai()}{t['cta_short']}</a>
  </div>
</header>

<main>

<section id="topo" class="wrap hero">
  <div class="hero-text">
    <p class="eyebrow">{t['eyebrow']}</p>
    <h1>{t['h1']}</h1>
    <p class="lead">{tx('lead')}</p>
    <div class="hero-actions">
      <a href="{general}" class="btn btn-primary btn-lg" target="_blank" rel="noopener">{wai(20)}{t['cta_long']}</a>
      <a href="#imoveis" class="btn btn-outline btn-lg">{tx('see_all')}</a>
    </div>
    {att_html}
    <ul class="proof-row">{proof}</ul>
  </div>
  <div class="hero-media">
    <picture><source srcset="{R}images/hero-sala.webp" type="image/webp"><img src="{R}images/hero-sala.jpg" alt="{t['hero_alt']}" width="908" height="1210" fetchpriority="high"></picture>
    <div class="hero-badge">
      <span class="hero-count">{N}</span>
      <div>
        <strong>{t['badge']}</strong>
        <span>{tx('updated')}</span>
      </div>
    </div>
  </div>
</section>

<section id="imoveis" class="band">
  <div class="wrap listings">
    <div class="section-head">
      <h2>{t['list_h']}</h2>
      <p>{t['list_p']}</p>
    </div>
    <div class="grid">
{CARDS}
    </div>
  </div>
</section>

<section id="como-funciona" class="wrap steps-section">
  <div class="section-head">
    <h2>{t['steps_h']}</h2>
  </div>
  <ol class="steps">{steps}
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

<section id="contato" class="wrap contact">
  <h2>{t['end_h']}</h2>
  <p>{t['end_p']}</p>
  <a href="{general}" class="btn btn-primary btn-xl" target="_blank" rel="noopener">{wai(20)}{t['cta_long']}</a>
</section>

</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-id">
      <span class="brand-name">Global Consultancy Partners Ltda</span>
      <span>CNPJ {CNPJ}</span>
    </div>
    <div class="footer-id footer-right">
      <span>{t['foot_tag']}</span>
      <a class="footer-wa" href="{general}" target="_blank" rel="noopener" aria-label="WhatsApp {WA_SHOW}">{wai(18)}{WA_SHOW}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</footer>

<a href="{general}" class="mobile-cta" target="_blank" rel="noopener">{wai(20)}{t['cta_short']}</a>

<script>
document.querySelectorAll('.gallery').forEach(function (g) {{
  var t = g.querySelector('.gallery-track'), c = g.querySelector('.gallery-count'), n = t.children.length;
  if (n < 2) {{ g.classList.add('single'); return; }}
  function idx() {{ return Math.round(t.scrollLeft / t.clientWidth); }}
  function go(d) {{ t.scrollTo({{ left: ((idx() + d + n) % n) * t.clientWidth, behavior: 'smooth' }}); }}
  g.querySelector('.prev').addEventListener('click', function () {{ go(-1); }});
  g.querySelector('.next').addEventListener('click', function () {{ go(1); }});
  t.addEventListener('scroll', function () {{ c.textContent = (idx() + 1) + ' / ' + n; }}, {{ passive: true }});
  t.addEventListener('keydown', function (e) {{ if (e.key === 'ArrowRight') {{ e.preventDefault(); go(1); }} if (e.key === 'ArrowLeft') {{ e.preventDefault(); go(-1); }} }});
}});
(function () {{
  var cta = document.querySelector('.mobile-cta'), hero = document.querySelector('.hero-actions');
  if (!cta || !hero || !('IntersectionObserver' in window)) {{ if (cta) cta.classList.add('show'); return; }}
  new IntersectionObserver(function (e) {{ cta.classList.toggle('show', !e[0].isIntersecting); }}).observe(hero);
}})();
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
