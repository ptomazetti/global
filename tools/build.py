from urllib.parse import quote
WA='5515997470301'
def wa(msg): return f'https://wa.me/{WA}?text={quote(msg)}'
def brl(v):
    s=f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')
    return 'R$ '+s
P=[
 dict(id='spettacolo-42',img='spettacolo-42.jpg',w=900,h=1199,alt='Spettacolo Patriani, apto. 42: sala com vista pela varanda panorâmica',tag='Studio alto padrão',name='Spettacolo Patriani',meta='Apto. 42 · 76 m² de área total',
  perks=['2 garagens cobertas e depósito de 10 m²','Varanda panorâmica, cama box Queen','Piscina com raia, SPA, sauna e academia'],rent=3490,condo=615.09,iptu=56.30,
  f='https://drive.google.com/drive/folders/1q39K2Jp_P_wErO56gb_jWGZT09iCpRCm?usp=sharing',v='https://drive.google.com/drive/folders/1lPg1uhrh6_9gQgG7jaKDxVGTWJAIPtrx?usp=drive_link',d='https://drive.google.com/file/d/1akjtOVeacGJNRz2Ihp5uc-KQfwCBWlxQ/view?usp=drive_link'),
 dict(id='alpha-club-j42',img='alpha-club-j42.jpg',w=900,h=675,alt='Alpha Club, apto. J42: sala com bar iluminado e bancada',tag='2 dormitórios c/ suíte',name='Alpha Club J42',meta='Apto. 42 · Bloco J · Campolim',
  perks=['Ar-condicionado 12.000 BTUs na suíte','Cama box Queen, Smart TV, cortina blackout','Varanda gourmet, condomínio clube'],rent=2890,condo=464.19,iptu=158.00,
  f='https://drive.google.com/drive/folders/1bPidYHmKlhAE6bBfmmKMkpROLZA144Wz?usp=drive_link',v='https://drive.google.com/drive/folders/1Aj7hwWm6NFKFlbf-Cg_wN6XHlmL7M8kM?usp=drive_link',d='https://drive.google.com/file/d/1W3QlSmMlkzd-SnY9_mjDsCZN_WANdPRY/view?usp=sharing'),
 dict(id='esplanada-102',img='esplanada-102.jpg',w=900,h=675,alt='Residencial Esplanada, apto. 102: sala integrada com cozinha',tag='3 dormitórios',name='Residencial Esplanada',meta='Apto. 102 · Bloco 2',
  perks=['Cozinha equipada, geladeira 440 L, cooktop e forno','Máquina lava e seca, ar-condicionado na sala','1 vaga, condomínio clube'],rent=2890,condo=500.00,iptu=105.33,
  f='https://drive.google.com/drive/folders/1A19Eb5ZPVLWmBcxqc6R4a2GPwvbjgVFB?usp=drive_link',v='https://drive.google.com/drive/folders/19i1YFcf9KCxrye3UG8FQDM-IXv_1g_qE?usp=drive_link',d='https://drive.google.com/file/d/19NxWZqBZ20AZ7AQVyDnz_o85rwfdnqPo/view?usp=sharing'),
 dict(id='alpha-club-i41',img='alpha-club-i41.jpg',w=900,h=675,alt='Alpha Club, apto. I41: sala com sofá e TV',tag='2 dormitórios c/ suíte',name='Alpha Club I41',meta='Apto. 41 · Bloco I · Campolim',
  perks=['Dois quartos com cama box de casal','Mesa de jantar para 4 lugares','Varanda gourmet, 1 vaga, condomínio clube'],rent=2790,condo=497.77,iptu=158.12,
  f='https://drive.google.com/drive/folders/1UxoTaZttGauF5RwCaPovwjylUFDpiMxK?usp=drive_link',v='https://drive.google.com/drive/folders/1ZqcbXnrIE4xuA2ob8gaRtECV8nynp88b?usp=drive_link',d='https://drive.google.com/file/d/1PBosWcqSD6zJ6Efxw_TIPX-IsAMZ3zzL/view?usp=drive_link'),
 dict(id='vida-plena-c65',img='vida-plena-c65.jpg',w=900,h=1199,alt='Vida Plena, apto. C65: sala com mesa de jantar',tag='2 dormitórios',name='Vida Plena C65',meta='Apto. 65 · Bloco C · Campolim',
  perks=['Armários planejados em todos os cômodos','Bancada para home office, iluminação LED','Condomínio com lazer completo'],rent=2790,condo=406.42,iptu=61.84,
  f='https://drive.google.com/drive/folders/1qV2qAFvA47z2pMG8QX_9GhA8e6oTtLZb?usp=drive_link',v='https://drive.google.com/drive/folders/1PODn9-X7koK7EUwgue70c9oIHWpFSGll?usp=drive_link',d='https://drive.google.com/file/d/1J17liUYRHgMADoPXDzAqgiYSOjdORVh1/view?usp=sharing'),
]
GAL={
 'spettacolo-42':['Sala com vista pela varanda panorâmica','Sala de estar com sofá e poltronas','Cozinha com armários planejados e cooktop','SPA com hidromassagem do condomínio','Fachada do Spettacolo Patriani'],
 'alpha-club-j42':['Sala com bar iluminado e bancada','Cozinha com geladeira, fogão e micro-ondas'],
 'esplanada-102':['Sala integrada com mesa de jantar','Cozinha com geladeira e micro-ondas','Dormitório com armário planejado'],
 'alpha-club-i41':['Sala com sofá e Smart TV','Cozinha equipada com máquina de lavar','Academia do condomínio','Piscina do condomínio'],
 'vida-plena-c65':['Sala com mesa de jantar','Cozinha com geladeira, fogão e micro-ondas','Dormitório com cama box e armário'],
}
WA_SVG=open('tools/icons/whatsapp.svg').read().split('d="')[1].split('"')[0]
AB_SVG=open('tools/icons/airbnb.svg').read().split('d="')[1].split('"')[0]
def wai(sz=18): return f'<svg class="logo" width="{sz}" height="{sz}" viewBox="0 0 24 24" aria-hidden="true"><path d="{WA_SVG}"/></svg>'
CAM='<svg width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>'
PLAY='<svg width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m10 8 6 4-6 4z"/></svg>'
DOC='<svg width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>'
CHECK='<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
general=wa('Olá! Vi o site da Global e quero agendar uma visita. Meu nome é: ')
broker=wa('Olá! Sou corretor(a) e quero agendar uma visita.\nNome:\nRG:\nCRECI:\nImóvel:\nDia e horário:')
cards=[]
for p in P:
    total=p['rent']+p['condo']+p['iptu']
    msg=wa(f"Olá! Vi o site da Global e quero visitar o {p['name']} ({brl(p['rent'])}). Meu nome é: ")
    perks=''.join(f'<li>{x}</li>' for x in p['perks'])
    alts=GAL[p['id']]; n=len(alts)
    slides=''.join(f'<picture class="slide"><source srcset="images/g/{p["id"]}-{i+1}.webp" type="image/webp"><img src="images/g/{p["id"]}-{i+1}.jpg" alt="{p["name"]}: {a}" loading="lazy" decoding="async" width="760" height="570"></picture>' for i,a in enumerate(alts))
    cards.append(f'''    <article class="card" id="{p['id']}">
      <div class="card-media gallery">
        <div class="gallery-track" tabindex="0" aria-label="Fotos do {p['name']}">{slides}</div>
        <span class="tag">{p['tag']}</span>
        <span class="gallery-count" aria-hidden="true">1 / {n}</span>
        <button class="gallery-btn prev" type="button" aria-label="Foto anterior">‹</button>
        <button class="gallery-btn next" type="button" aria-label="Próxima foto">›</button>
      </div>
      <div class="card-body">
        <div>
          <h3>{p['name']}</h3>
          <p class="meta">{p['meta']}</p>
        </div>
        <ul class="perks">{perks}</ul>
        <div class="price">
          <p class="price-value">{brl(p['rent']).replace(',00','')}<span> /mês de aluguel</span></p>
          <p class="price-extra">Condomínio {brl(p['condo'])} · IPTU {brl(p['iptu'])}</p>
          <p class="price-total">Total mensal: {brl(total)}</p>
        </div>
        <a class="btn btn-primary btn-block" href="{msg}" target="_blank" rel="noopener">{wai()}Quero visitar este</a>
        <div class="card-links">
          <a href="{p['f']}" target="_blank" rel="noopener">{CAM}Fotos</a>
          <a href="{p['v']}" target="_blank" rel="noopener">{PLAY}Vídeo</a>
          <a href="{p['d']}" target="_blank" rel="noopener">{DOC}Descrição</a>
        </div>
      </div>
    </article>''')
CARDS='\n\n'.join(cards)
FAV="data:image/svg+xml,"+quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#1D5C46"/><text x="16" y="22" font-family="Arial" font-weight="700" font-size="17" fill="#fff" text-anchor="middle">G</text></svg>')
import json
LD={"@context":"https://schema.org","@type":"ItemList","name":"Apartamentos mobiliados para locação","itemListElement":[
 {"@type":"ListItem","position":i+1,"item":{"@type":"Offer","name":f"{p['name']} · {p['tag']}","priceCurrency":"BRL","price":f"{p['rent']:.2f}","availability":"https://schema.org/InStock","seller":{"@type":"Organization","name":"Global Consultancy Partners Ltda","taxID":"50.945.139/0001-86","telephone":"+5515997470301"}}} for i,p in enumerate(P)]}
LDJ=json.dumps(LD,ensure_ascii=False)
html=f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Apartamentos mobiliados em Sorocaba a partir de R$ 2.790 | Global</title>
<meta name="description" content="5 apartamentos mobiliados prontos para morar em Sorocaba, de studio a 3 dormitórios. Aluguel a partir de R$ 2.790. Agende sua visita pelo WhatsApp.">
<meta property="og:type" content="website">
<meta property="og:title" content="Apartamentos mobiliados em Sorocaba, prontos para morar">
<meta property="og:description" content="5 apartamentos disponíveis, de studio a 3 dormitórios. Aluguel a partir de R$ 2.790. Agende sua visita pelo WhatsApp.">
<meta property="og:locale" content="pt_BR">
<link rel="icon" href="{FAV}">
<link rel="preload" as="image" href="images/hero-sala.webp" type="image/webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&amp;family=Manrope:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">{LDJ}</script>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a href="#topo" class="brand">
      <span class="brand-mark" aria-hidden="true">G</span>
      <span class="brand-name">Global Consultancy Partners</span>
    </a>
    <nav aria-label="Principal" class="nav">
      <a href="#imoveis">Apartamentos</a>
      <a href="#como-funciona">Como funciona</a>
      <a href="#duvidas">Dúvidas</a>
      <a href="#corretores">Corretores</a>
    </nav>
    <a href="{general}" class="btn btn-primary btn-sm header-cta" target="_blank" rel="noopener">{wai()}Agendar visita</a>
  </div>
</header>

<main>

<section id="topo" class="wrap hero">
  <div class="hero-text">
    <p class="eyebrow">Locação mobiliada em Sorocaba</p>
    <h1>Apartamento mobiliado. Você só traz a mala.</h1>
    <p class="lead">5 apartamentos prontos para morar, de studio a 3 dormitórios, em condomínios com lazer. Aluguel a partir de R$ 2.790. Visite antes de decidir.</p>
    <div class="hero-actions">
      <a href="{general}" class="btn btn-primary btn-lg" target="_blank" rel="noopener">{wai(20)}Agendar visita pelo WhatsApp</a>
      <a href="#imoveis" class="btn btn-outline btn-lg">Ver os 5 apartamentos</a>
    </div>
    <ul class="proof-row">
      <li>{CHECK}Pintado e higienizado a cada locação</li>
      <li>{CHECK}3 opções de garantia</li>
      <li>{CHECK}Fotos, vídeo e descrição de cada imóvel</li>
    </ul>
  </div>
  <div class="hero-media">
    <picture><source srcset="images/hero-sala.webp" type="image/webp"><img src="images/hero-sala.jpg" alt="Sala mobiliada do Spettacolo Patriani com sofá, poltronas e tapete" width="908" height="1210" fetchpriority="high"></picture>
    <div class="hero-badge">
      <span class="hero-count">5</span>
      <div>
        <strong>disponíveis hoje</strong>
        <span>Lista atualizada em 1 de novembro de 2026</span>
      </div>
    </div>
  </div>
</section>

<section id="imoveis" class="band">
  <div class="wrap listings">
    <div class="section-head">
      <h2>Escolha o seu e marque a visita</h2>
      <p>Valores completos à vista: aluguel, condomínio e IPTU. Sem surpresa no contrato.</p>
    </div>
    <div class="grid">
{CARDS}
    </div>
  </div>
</section>

<section id="como-funciona" class="wrap steps-section">
  <div class="section-head">
    <h2>Da visita às chaves em 3 passos</h2>
  </div>
  <ol class="steps">
    <li>
      <span class="step-n">1</span>
      <h3>Escolha e visite</h3>
      <p>Toque em "Quero visitar este" no apartamento. A mensagem já vai pronta no WhatsApp, com o nome do imóvel.</p>
    </li>
    <li>
      <span class="step-n">2</span>
      <h3>Escolha a garantia</h3>
      <p>Seguro fiança, caução de 3 aluguéis ou fiador. Você usa a que for mais simples para você.</p>
    </li>
    <li>
      <span class="step-n">3</span>
      <h3>Entre com a mala</h3>
      <p>Móveis, cozinha equipada e eletrodomésticos já estão lá. O apartamento é pintado e higienizado antes de você chegar.</p>
    </li>
  </ol>
  <div class="compare">
    <div class="compare-col">
      <h3>Alugar um apartamento vazio</h3>
      <ul>
        <li>Comprar sofá, cama, mesa e cortinas</li>
        <li>Comprar geladeira, fogão, micro-ondas e máquina de lavar</li>
        <li>Pagar frete, montagem e instalação</li>
        <li>Semanas até a casa ficar pronta</li>
      </ul>
    </div>
    <div class="compare-col compare-win">
      <h3>Alugar com a Global</h3>
      <ul>
        <li>Móveis e armários planejados já instalados</li>
        <li>Eletrodomésticos funcionando</li>
        <li>Apartamento pintado e higienizado</li>
        <li>Você muda sem esperar móveis chegarem</li>
      </ul>
    </div>
  </div>
</section>

<section id="duvidas" class="band">
  <div class="wrap faq-section">
    <div class="section-head">
      <h2>Perguntas antes de visitar</h2>
    </div>
    <div class="faq">
      <details>
        <summary>Quais garantias vocês aceitam?</summary>
        <p>Seguro fiança, caução de 3 aluguéis ou fiador.</p>
      </details>
      <details>
        <summary>O valor do aluguel inclui condomínio e IPTU?</summary>
        <p>Não. Condomínio e IPTU são cobrados à parte. Cada apartamento mostra os três valores e o total mensal, para você comparar sem surpresa.</p>
      </details>
      <details>
        <summary>O que exatamente vem no apartamento?</summary>
        <p>Cada imóvel tem uma descrição completa com a lista de móveis e eletrodomésticos. Toque em "Descrição" no card do apartamento.</p>
      </details>
      <details>
        <summary>O apartamento é limpo antes de eu entrar?</summary>
        <p>Sim. A cada nova locação, o apartamento é pintado e higienizado.</p>
      </details>
      <details>
        <summary>Como agendo uma visita?</summary>
        <p>Pelo WhatsApp <a href="{general}" target="_blank" rel="noopener">+55 (15) 99747-0301</a>. Diga qual apartamento e o melhor dia e horário para você.</p>
      </details>
      <details>
        <summary>Preciso de uma estadia curta. Vocês têm?</summary>
        <p class="airbnb-line"><svg class="logo airbnb" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="{AB_SVG}"/></svg>Sim, para estadias curtas procure por Global Flats no Airbnb.</p>
      </details>
    </div>
  </div>
</section>

<section id="corretores" class="dark">
  <div class="wrap brokers">
    <div class="brokers-text">
      <p class="eyebrow eyebrow-gold">Para corretores parceiros</p>
      <h2>Feche locação sem montar material.</h2>
      <p>Cada apartamento já tem fotos, vídeo e descrição prontos para você enviar ao cliente. Use os links dos cards ou peça o material completo.</p>
    </div>
    <div class="notice">
      <h3>Para agendar uma visita</h3>
      <p>Envie em uma única mensagem:</p>
      <ul class="chips">
        <li>Nome</li><li>RG</li><li>CRECI</li><li>Imóvel</li><li>Dia e horário</li>
      </ul>
      <a href="{broker}" class="btn btn-primary btn-block" target="_blank" rel="noopener">{wai()}Enviar pedido de visita</a>
      <p class="small">O botão abre o WhatsApp com esses campos já preenchidos.</p>
    </div>
  </div>
</section>

<section id="contato" class="wrap contact">
  <h2>Gostou de um? Marque a visita hoje.</h2>
  <p>Cada apartamento é único. Quando ele é alugado, sai da lista.</p>
  <a href="{general}" class="btn btn-primary btn-xl" target="_blank" rel="noopener">{wai(20)}Agendar visita pelo WhatsApp</a>
  <p class="phone">+55 (15) 99747-0301</p>
</section>

</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-id">
      <span class="brand-name">Global Consultancy Partners Ltda</span>
      <span>CNPJ 50.945.139/0001-86</span>
    </div>
    <div class="footer-id footer-right">
      <span>Locação de apartamentos mobiliados · Sorocaba</span>
      <a href="{general}" target="_blank" rel="noopener">WhatsApp +55 (15) 99747-0301</a>
    </div>
  </div>
</footer>

<a href="{general}" class="mobile-cta" target="_blank" rel="noopener">{wai(20)}Agendar visita</a>

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
open('index.html','w',encoding='utf-8').write(html)
for p in P: print(p['name'], brl(p['rent']+p['condo']+p['iptu']))
