# Собирает index.html из src/site-template.html и src/assets (фото, рендеры, 3D-модель)
import base64, os, re, sys, shutil, unicodedata
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); src=os.path.join(root,'src'); assets=os.path.join(src,'assets')
b=lambda f: base64.b64encode(open(f,'rb').read()).decode()
files={unicodedata.normalize('NFC',f):f for f in os.listdir(assets)}
def img(key):
    key=unicodedata.normalize('NFC',key); name=key.replace('render:','render-')
    for ext in ('.jpg','.png'):
        if name+ext in files:
            f=os.path.join(assets,files[name+ext]); mime='image/jpeg' if ext=='.jpg' else 'image/png'
            return f'data:{mime};base64,'+b(f)
    raise SystemExit('missing asset: '+key)
t=open(os.path.join(src,'site-template.html'),encoding='utf-8').read()
import json; sys.path.insert(0,src); from zsvg import zsvg_light, zsvg_dark
logo=open(os.path.join(root,'логотип','знак-red-dark.svg'),encoding='utf-8').read().replace('width="200" height="200"','width="34" height="34"').replace('\n','')
imgs={}
for f in os.listdir(assets):
    k=unicodedata.normalize('NFC',f); 
    if k.endswith('.jpg') or k.endswith('.png'): imgs[k.rsplit('.',1)[0].replace('render-','render:')]=img(k.rsplit('.',1)[0].replace('render-','render:'))
t=t.replace('{{LOGO}}',logo).replace('{{IMGS}}',json.dumps(imgs,ensure_ascii=False)).replace('{{ZSVG}}',zsvg_light())
t=re.sub(r'\{\{IMG:([^}]+)\}\}', lambda m: img(m.group(1)), t)
t=t.replace('{{TREATER}}', b(os.path.join(assets,'treater.glb')))
vid=os.path.join(assets,'hero.mp4')
t=t.replace('{{VIDEO}}', ('data:video/mp4;base64,'+b(vid)) if os.path.exists(vid) else '')
out=os.path.join(root,'index.html'); open(out,'w',encoding='utf-8').write(t)
print('built %s %.1f MB'%(out, os.path.getsize(out)/1e6))
