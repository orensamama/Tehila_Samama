import base64, os

def b64(path):
    with open(path,'rb') as f:
        return base64.b64encode(f.read()).decode()

folder = r'C:\Users\officeasher\Desktop\פרויקטים קלוד\אתר תהילה\תמונות'
hero   = b64(os.path.join(folder,'WhatsApp Image 2026-06-16 at 21.08.25.jpeg'))
about1 = b64(os.path.join(folder,'WhatsApp Image 2026-06-16 at 21.08.27 (2).jpeg'))
about2 = b64(os.path.join(folder,'WhatsApp Image 2026-06-16 at 21.08.27.jpeg'))

html = open(r'C:\Users\officeasher\Desktop\פרויקטים קלוד\אתר תהילה\template.html',encoding='utf-8').read()
html = html.replace('HERO_B64', hero).replace('ABOUT1_B64', about1).replace('ABOUT2_B64', about2)

out = r'C:\Users\officeasher\Desktop\פרויקטים קלוד\אתר תהילה\index.html'
with open(out,'w',encoding='utf-8') as f:
    f.write(html)
print('Done,', len(html), 'bytes')
