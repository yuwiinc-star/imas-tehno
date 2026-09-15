import re,sys
p='src/site-template.html'; s=open(p,encoding='utf-8').read()
rep=[
 (":root{--sand:#FFFFFF;--cream:#F5F5F3;--sand-2:#E9E9E6;--ink:#151715;--ink-2:#1F2220;--red:#C8352B;--red-deep:#A52A22;--gold:#C8352B;",
  ":root{--sand:#0F1010;--cream:#161717;--sand-2:#1E1F1E;--ink:#0B0C0B;--ink-2:#161717;--red:#E23D31;--red-deep:#C42F25;--gold:#E23D31;--card:#1A1B1A;--r:18px;"),
 ("--txt:#171717;--muted:#6B6B68;--muted-l:#A3A3A0;--rule:rgba(23,23,23,.10);--rule-l:rgba(255,255,255,.16);",
  "--txt:#F2F2F0;--muted:#9C9C98;--muted-l:#7C7C78;--rule:rgba(255,255,255,.09);--rule-l:rgba(255,255,255,.12);"),
 ("h1,h2,h3.d{font-family:var(--display);font-weight:700;text-transform:uppercase;line-height:1.02;letter-spacing:-.01em;margin:0;text-wrap:balance}",
  "h1,h2,h3.d{font-family:var(--display);font-weight:700;text-transform:none;line-height:1.08;letter-spacing:-.015em;margin:0;text-wrap:balance}"),
 ("h1{font-size:clamp(2rem,4.2vw,4.4rem)}\n  h2{font-size:clamp(1.4rem,2.4vw,2.4rem)}","h1{font-size:clamp(1.9rem,3.6vw,3.6rem)}\n  h2{font-size:clamp(1.35rem,2.2vw,2.1rem)}"),
 (".lead{color:var(--muted);max-width:52ch;font-size:1.05em}\n  .dark .lead{color:#D9D4C8}",".lead{color:var(--muted);max-width:52ch;font-size:1.05em}\n  .dark .lead{color:#C9C9C5}"),
 (".nav{position:sticky;top:0;z-index:30;background:rgba(255,255,255,.94);backdrop-filter:blur(8px);color:var(--txt);border-bottom:1px solid var(--rule);",
  ".nav{position:sticky;top:0;z-index:30;background:rgba(15,16,16,.92);backdrop-filter:blur(10px);color:var(--txt);border-bottom:1px solid var(--rule);"),
 (".nav ul a{opacity:.7;padding:6px 0;border-bottom:2px solid transparent}.nav ul a:hover{opacity:1}.nav ul a.on{opacity:1;border-color:var(--red)}\n  .nav .tel{color:var(--txt)}",
  ".nav ul a{opacity:.7;padding:6px 0;border-bottom:2px solid transparent;text-transform:none;letter-spacing:0;font-size:14px}.nav ul a:hover{opacity:1}.nav ul a.on{opacity:1;border-color:var(--red)}\n  .nav .tel{color:var(--txt);border:1px solid var(--rule-l);padding:10px 16px;border-radius:12px}\n  .nav .catbtn{display:inline-flex;align-items:center;gap:8px;background:#fff;color:#0F1010;border-radius:12px;padding:10px 16px;font-size:13px;font-weight:600;text-transform:none;letter-spacing:0}\n  .nav .lft{display:flex;align-items:center;gap:18px}\n  @media(max-width:900px){.nav .catbtn{display:none}}"),
 (".btn{display:inline-flex;align-items:center;gap:12px;padding:15px 22px 15px 24px;font-weight:600;font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--rule);color:var(--txt);",
  ".btn{display:inline-flex;align-items:center;gap:12px;padding:15px 22px;font-weight:600;font-size:14px;letter-spacing:0;text-transform:none;border-radius:12px;border:1px solid var(--rule-l);color:var(--txt);"),
 (".btn.ghost:hover{background:var(--ink);color:var(--cream);border-color:var(--ink)}",".btn.ghost{background:#1F2120}.btn.ghost:hover{background:#2A2C2B;border-color:#2A2C2B}"),
 (".dark .btn,.over .btn{color:var(--cream);border-color:rgba(251,249,244,.45)}.dark .btn.ghost:hover,.over .btn.ghost:hover{background:var(--cream);color:var(--ink);border-color:var(--cream)}",
  ".dark .btn,.over .btn{color:#fff;border-color:rgba(255,255,255,.2)}.over .btn.ghost{background:rgba(255,255,255,.12)}.dark .btn.ghost:hover,.over .btn.ghost:hover{background:rgba(255,255,255,.22)}"),
 (".sec.white{background:var(--cream)}",".sec.white{background:var(--cream)}\n  .crumbs{font-size:13px;color:var(--muted);display:flex;gap:10px;align-items:center;margin-bottom:26px}.crumbs a:hover{color:var(--txt)}"),
 (".card{background:#fff;border:1px solid var(--rule);display:flex;flex-direction:column;min-width:0;color:var(--txt);transition:border-color .2s,transform .2s}\n  a.card{cursor:pointer}a.card:hover{border-color:var(--ink);transform:translateY(-2px)}",
  ".card{background:var(--card);border:1px solid var(--rule);border-radius:var(--r);display:flex;flex-direction:column;min-width:0;color:var(--txt);transition:border-color .2s,transform .2s;overflow:hidden}\n  a.card{cursor:pointer}a.card:hover{border-color:rgba(255,255,255,.28);transform:translateY(-2px)}\n  .ph.cut{aspect-ratio:4/3;background:linear-gradient(180deg,#202221,#161717);display:grid;place-items:center;padding:6%}\n  .ph.cut img{width:100%;height:100%;object-fit:contain;filter:none}"),
 (".cells{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--rule);border:1px solid var(--rule)}",
  ".cells{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}"),
 (".cells>div{background:#fff;padding:24px 22px 26px}",".cells>div{background:var(--card);border:1px solid var(--rule);border-radius:var(--r);padding:24px 22px 26px}"),
 (".split{display:grid;grid-template-columns:1fr;gap:0;align-items:stretch;background:#fff;border:1px solid var(--rule)}",".split{display:grid;grid-template-columns:1fr;gap:0;align-items:stretch;background:var(--card);border:1px solid var(--rule);border-radius:var(--r)}"),
 (".split .txt p{color:#4a4741;font-size:.98em}",".split .txt p{color:#C9C9C5;font-size:.98em}"),
 (".split ol,.split ul{margin:0;padding-left:18px;color:#4a4741;",".split ol,.split ul{margin:0;padding-left:18px;color:#C9C9C5;"),
 (".cta .box{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:40px;background:#fff;border:1px solid var(--rule);",".cta .box{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:40px;background:var(--card);border:1px solid var(--rule);border-radius:var(--r);"),
 (".f input,.f textarea,.f select{font-family:var(--body);font-size:15px;color:var(--txt);background:var(--cream);border:1px solid var(--rule);padding:13px 14px;width:100%}",
  ".f input,.f textarea,.f select{font-family:var(--body);font-size:15px;color:var(--txt);background:#111212;border:1px solid var(--rule-l);border-radius:10px;padding:13px 14px;width:100%}"),
 (".f input:focus,.f textarea:focus,.f select:focus{border-color:var(--ink);outline:none}",".f input:focus,.f textarea:focus,.f select:focus{border-color:#fff;outline:none}"),
 (".kont .info{background:#fff;",".kont .info{background:var(--card);border-radius:var(--r);"),(".kont .fbox{background:#fff;",".kont .fbox{background:var(--card);border-radius:var(--r);"),
 (".mspec{border:1px solid var(--rule);background:#fff;",".mspec{border:1px solid var(--rule);background:var(--card);border-radius:var(--r);"),
 (".stage{position:relative;border:1px solid var(--rule);background:#fff;",".stage{position:relative;border:1px solid var(--rule);background:var(--card);border-radius:var(--r);"),
 (".stage .ctl button{width:38px;height:38px;border:1px solid var(--rule);background:rgba(251,249,244,.92);color:var(--txt);",".stage .ctl button{width:38px;height:38px;border:1px solid var(--rule-l);background:rgba(20,21,20,.9);color:#fff;border-radius:10px;"),
 (".stage .ctl button:hover{background:var(--ink);color:var(--cream)}",".stage .ctl button:hover{background:#fff;color:#111}"),
 ("text-transform:uppercase;color:var(--muted);background:#fff}","text-transform:uppercase;color:var(--muted);background:var(--card)}"),
 (".msel button[aria-pressed=\"true\"]{color:var(--cream);background:var(--ink);border-color:var(--ink)}",".msel button[aria-pressed=\"true\"]{color:#0F1010;background:#fff;border-color:#fff}"),
 (".msel button{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;background:transparent;border:1px solid var(--rule);color:var(--muted);padding:10px 16px;",".msel button{font-family:var(--body);font-size:14px;letter-spacing:0;text-transform:none;background:var(--card);border:1px solid var(--rule-l);color:var(--txt);border-radius:12px;padding:10px 16px;"),
 (".tbtn{width:38px;height:38px;border:1px solid var(--rule);background:transparent;color:var(--txt);",".tbtn{width:38px;height:38px;border:1px solid var(--rule-l);background:var(--card);color:var(--txt);border-radius:10px;"),
 (".tbtn:hover{background:var(--ink);color:var(--cream)}",".tbtn:hover{background:#fff;color:#111}"),
 ("input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:1px;background:rgba(27,27,25,.35);","input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:1px;background:rgba(255,255,255,.35);"),
 ("input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:18px;height:18px;border-radius:50%;background:var(--ink);border:3px solid var(--sand);box-shadow:0 0 0 1px var(--ink);cursor:grab}","input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:18px;height:18px;border-radius:50%;background:#fff;border:3px solid var(--sand);box-shadow:0 0 0 1px #fff;cursor:grab}"),
 (".slogan{margin-top:var(--gap);padding:22px 26px;border-left:3px solid var(--red);background:#fff;",".slogan{margin-top:var(--gap);padding:22px 26px;border-left:3px solid var(--red);background:var(--card);border-radius:0 var(--r) var(--r) 0;"),
 (".tbl{overflow-x:auto;border:1px solid var(--rule);background:#fff;padding:0 20px}",".tbl{overflow-x:auto;border:1px solid var(--rule);background:var(--card);border-radius:var(--r);padding:0 20px}"),
 (".pitem p{color:#4a4741;font-size:.92em}",".pitem p{color:#C9C9C5;font-size:.92em}"),
 (".cells .n{font-family:var(--mono);font-size:12px;color:var(--red);letter-spacing:.08em}",".cells .n{font-family:var(--mono);font-size:12px;color:var(--red);letter-spacing:.08em}\n  .cells h3{color:var(--txt)}"),
 (".hero .veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,23,21,.35) 0%,rgba(21,23,21,.15) 35%,rgba(21,23,21,.8) 78%,rgba(21,23,21,.94) 100%)}",
  ".hero .veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,16,16,.35) 0%,rgba(15,16,16,.15) 35%,rgba(15,16,16,.85) 78%,rgba(15,16,16,.98) 100%)}\n  .phero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:40px;align-items:center;padding:28px 0 20px;min-height:min(72vh,680px)}\n  .phero .cut{width:100%;aspect-ratio:4/3;display:grid;place-items:center}\n  .phero .cut img{width:100%;height:100%;object-fit:contain;filter:drop-shadow(0 30px 60px rgba(0,0,0,.6))}\n  .phero h1{max-width:16ch}\n  @media(max-width:900px){.phero{grid-template-columns:1fr;min-height:0}.phero .cut{order:-1;aspect-ratio:3/2}}"),
 (".hero.compact{min-height:0;background:linear-gradient(135deg,#1a1d1a,#2f332f)}\n  .hero.compact .in{padding-top:72px}",".hero.compact{min-height:0;background:transparent}\n  .hero.compact .in{padding-top:72px}"),
 ('''  <a class="brand" href="#/">{{LOGO}}<span>ИМАС<em>-ТЕХНО</em></span></a>
  <ul>''','''  <div class="lft"><a class="brand" href="#/">{{LOGO}}<span>ИМАС<em>-ТЕХНО</em></span></a><a class="catbtn" href="#/katalog">Каталог <span aria-hidden="true">≡</span></a></div>
  <ul>'''),
 ("""const P=[
 {id:'ayveri', link:true, cat:'Протравливание', name:'Протравитель семян Айвери', img:'айвери-фронт', pos:'50% 45%', v:'6,5', u:'т/ч'},
 {id:'zet', cat:'Транспортировка', name:'Транспортёр с качающимися ковшами', img:'линия-вертикаль-1', pos:'18% 50%', v:'20', u:'м³/ч'},
 {id:'mera', cat:'Фасовка', name:'Дозаторы для сыпучих продуктов МЕРА', img:'мера-фото', pos:'50% 40%', v:'1000', u:'кг'},
];""","""const P=[
 {id:'ayveri', link:true, cat:'Протравливание', name:'Протравитель семян Айвери', img:'cut-ayveri', v:'6,5', u:'т/ч'},
 {id:'zet', cat:'Транспортировка', name:'Транспортёр с качающимися ковшами', img:null, v:'20', u:'м³/ч'},
 {id:'mera', cat:'Фасовка', name:'Дозаторы для сыпучих продуктов МЕРА', img:'cut-mera', v:'1000', u:'кг'},
];"""),
 ("""  a.innerHTML=`<div class="cb"><div><div class="cat">${p.cat}</div><h3>${p.name}</h3></div>""","""  const media=(p.img&&withImg)?`<div class="ph cut"><img src="${IMG[p.img]}" alt="${p.name}" loading="lazy"></div>`:'';
  a.innerHTML=`${media}<div class="cb"><div><div class="cat">${p.cat}</div><h3>${p.name}</h3></div>"""),
 ("function card(p){","function card(p,withImg){"),
 ("document.querySelectorAll('[data-cards]').forEach(g=>P.forEach(p=>g.appendChild(card(p))));","document.querySelectorAll('[data-cards]').forEach(g=>P.forEach(p=>g.appendChild(card(p, g.classList.contains('grid')))));"),
 (".cb h3{font-family:var(--display);font-weight:700;text-transform:uppercase;font-size:1.15rem;line-height:1.1;margin:0;letter-spacing:-.005em}",".cb h3{font-family:var(--display);font-weight:700;text-transform:none;font-size:1.05rem;line-height:1.15;margin:0;letter-spacing:-.01em}"),
 (".cb .cat{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--red)}",".cb .cat{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--red)}\n  .cb .kv span{color:#fff}"),
]
miss=[]
for a,b in rep:
    if a in s: s=s.replace(a,b)
    else: miss.append(a[:70])
# product hero markup
i=s.index('  <!-- 1 -->\n  <section class="hero over compact">'); j=s.index('</section>',i)+len('</section>')
phero='''  <!-- 1 -->
  <section class="w">
    <div class="crumbs" style="margin-top:22px"><a href="#/">Главная</a><span>›</span><a href="#/katalog">Каталог</a><span>›</span><span>Протравитель семян Айвери</span></div>
    <div class="phero">
      <div><div class="mono" style="color:var(--red)">Протравливание · порционный</div>
        <h1 style="margin-top:12px">Протравитель семян Айвери</h1>
        <p class="lead" style="margin-top:16px">Порционная машина с дозированием по убыли веса. Четыре типоразмера от 1 до 10 т/ч, флагман R-700.</p>
        <div class="acts" style="margin-top:26px"><a class="btn primary" href="#/kontakty">Запросить цену <span class="plus">+</span></a><a class="btn ghost" href="#conf">Конфигуратор <span class="plus">↓</span></a></div></div>
      <div class="cut"><img src="{{IMG:cut-ayveri}}" alt="Протравитель Айвери, 3D-рендер"></div>
    </div>
  </section>'''
s=s[:i]+phero+s[j:]
open(p,'w',encoding='utf-8').write(s)
print('applied; missed:', miss)
