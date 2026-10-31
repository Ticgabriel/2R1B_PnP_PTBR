#!/usr/bin/env python3
"""Gera frentes/versos A4 a partir das cartas LaTeX traduzidas.
Requer Python 3 e reportlab. Execute a partir de qualquer diretório.
"""
from pathlib import Path
import re, json, hashlib, zipfile
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'impressao'; OUT.mkdir(exist_ok=True)
W,H=297*mm,210*mm
CW,CH,GAP=60*mm,90*mm,3*mm
X=(W-4*CW-3*GAP)/2; Y=(H-2*CH-GAP)/2
COLORS={'red':('#a31b29','#fff2f3','VERMELHA','V'), 'blue':('#153f8f','#eff5ff','AZUL','A'), 'grey':('#414852','#f2f3f5','CINZA','?'), 'purple':('#75228d','#faf0ff','ROXA','?')}

def group(s,p):
    assert s[p]=='{'
    start=p+1; depth=1;p+=1
    while depth:
        if s[p]=='{' and s[p-1]!='\\':depth+=1
        if s[p]=='}' and s[p-1]!='\\':depth-=1
        p+=1
    return s[start:p-1],p

def cards():
    groups=[]
    for f in sorted((ROOT/'src').glob('*.tex')):
        s=f.read_text(); deck=[]
        for m in re.finditer(r'\\(red|blue|grey|purple)card\s*\{',s):
            p=m.end()-1;args=[]
            for _ in range(3):
                while s[p].isspace():p+=1
                value,p=group(s,p);args.append(value)
            name,motto,body=args
            body=body.replace(r'\\[3mm]', '\n').replace('``','“').replace("''",'”')
            assert '\\' not in body,body
            deck.append(dict(team=m[1],name=name,motto=motto,body=body,source=f.name))
        groups.append(deck)
    assert sum(map(len,groups))==80
    return groups

def pos(slot):
    row,col=divmod(slot,4)
    return X+col*(CW+GAP),Y+(1-row)*(CH+GAP)

def marks(c,x,y):
    c.setStrokeColor(HexColor('#777777'));c.setLineWidth(.25)
    d=.6*mm;n=.8*mm
    for xx in (x,x+CW):
        c.line(xx,y-d,xx,y-d-n);c.line(xx,y+CH+d,xx,y+CH+d+n)
    for yy in (y,y+CH):
        c.line(x-d,yy,x-d-n,yy);c.line(x+CW+d,yy,x+CW+d+n,yy)

def paragraph(c,text,x,top,width,size=10,leading=13,bold=False,color='#17202a'):
    style=ParagraphStyle('card',fontName='Helvetica-Bold' if bold else 'Helvetica',fontSize=size,leading=leading,textColor=HexColor(color),spaceAfter=0)
    p=Paragraph(escape(text).replace('\n','<br/><br/>'),style)
    _,h=p.wrap(width,CH);p.drawOn(c,x,top-h)
    return top-h

def face(c,card,x,y):
    dark,light,team,symbol=COLORS[card['team']]
    c.setFillColor(HexColor(light));c.rect(x,y,CW,CH,fill=1,stroke=0)
    c.setFillColor(HexColor(dark));c.rect(x,y+CH-17*mm,CW,17*mm,fill=1,stroke=0);c.rect(x,y,CW,10*mm,fill=1,stroke=0)
    paragraph(c,card['name'],x+4*mm,y+CH-4*mm,CW-8*mm,12,14,True,'#ffffff')
    c.setFillColor(HexColor('#ffffff'));c.setFont('Helvetica-Bold',10);c.drawString(x+4*mm,y+3.6*mm,'EQUIPE '+team)
    c.setFont('Helvetica-Bold',13);c.drawRightString(x+CW-3*mm,y+3.2*mm,symbol)
    top=paragraph(c,card['motto'],x+4*mm,y+CH-21*mm,CW-8*mm,9,11,True)
    # Todos os textos usam o mesmo corpo. O assert impede cortes silenciosos.
    bottom=paragraph(c,card['body'],x+4*mm,top-3*mm,CW-8*mm,9.5,12)
    assert bottom>=y+13*mm,(card['name'],bottom-y)
    c.setStrokeColor(HexColor(dark));c.setLineWidth(.35);c.rect(x,y,CW,CH,fill=0,stroke=1)
    marks(c,x,y)

def back(c,x,y):
    c.setFillColor(HexColor('#f1f1ed'));c.rect(x,y,CW,CH,fill=1,stroke=0)
    c.setStrokeColor(HexColor('#20262d'));c.setLineWidth(1.2);c.rect(x+3*mm,y+3*mm,CW-6*mm,CH-6*mm,fill=0,stroke=1)
    c.setFillColor(HexColor('#20262d'))
    for yy in [y+CH/2+12*mm,y+CH/2-12*mm]:
        c.saveState();c.translate(x+CW/2,yy)
        if yy<y+CH/2:c.rotate(180)
        c.setFont('Helvetica-Bold',15);c.drawCentredString(0,0,'DUAS SALAS')
        c.setFont('Helvetica-Bold',12);c.drawCentredString(0,-6*mm,'E UMA BOMBA')
        c.restoreState()
    c.setStrokeColor(HexColor('#20262d'));c.rect(x,y,CW,CH,fill=0,stroke=1)
    marks(c,x,y)

def deck_pdf(filename,sheets):
    path=OUT/filename;c=canvas.Canvas(str(path),pagesize=(W,H),pageCompression=1)
    c.setTitle(filename.replace('_',' ')); c.setAuthor('Adaptação comunitária de drFerg/2R1B_PnP')
    layout=[]
    for number,sheet in enumerate(sheets,1):
        locations=[]
        for i,card in enumerate(sheet):
            x,y=pos(i);face(c,card,x,y)
            locations.append({'name':card['name'],'team':card['team'],'front_mm':[x/mm,y/mm,60,90],'back_mm':[(W-x-CW)/mm,y/mm,60,90]})
        c.showPage()
        # Espelho horizontal: A4 paisagem com virada na borda curta.
        for i,card in enumerate(sheet):
            x,y=pos(i);back(c,W-x-CW,y)
        c.showPage();layout.append({'sheet':number,'cards':locations})
    c.save();return layout

def guide():
    c=canvas.Canvas(str(OUT/'Guia_Impressao_PTBR_R02.pdf'),pagesize=(210*mm,297*mm));c.setTitle('Guia de impressão PT-BR')
    y=277*mm
    lines=[('Duas salas e uma bomba',18,True),('Guia de impressão - revisão 02',12,False),
    ('Configuração da impressora',14,True),('Papel A4 em paisagem. Escala 100% / tamanho real. Desative ajustar à página. Imprima todas as páginas, frente e verso, com virada na BORDA CURTA.',11,False),
    ('Teste primeiro a primeira folha (páginas 1 e 2). Contra a luz, confirme se frente, verso e marcas de corte coincidem. Os versos já estão espelhados horizontalmente: não aplique outro espelhamento.',11,False),
    ('Recorte pelas marcas, mantendo as cartas em 60 × 90 mm. A precisão depende da impressora; o alinhamento digital foi conferido, mas não substitui esse teste físico.',11,False),
    ('Qual arquivo imprimir?',14,True),('Kit_11_Jogadores_PTBR_R02.pdf: 4 páginas, equivalentes a 2 folhas duplex. Use todas as 11 cartas: Bombista, 4 vermelhas comuns, Presidente, 4 azuis comuns e Apostador. Separe as cartas de forma aleatória entre os jogadores.',11,False),
    ('Cartas_Completas_PTBR_R02.pdf: 22 páginas, equivalentes a 11 folhas duplex. Contém as 80 cartas do projeto-fonte, inclusive repetições. NÃO distribua todas numa mesma partida. Selecione os papéis e as quantidades para a composição desejada.',11,False),
    ('Papel e acabamento',14,True),('Para frente e verso, prefira papel opaco compatível com a impressora. Uma alternativa é papel comum dentro de sleeves com uma carta opaca de apoio. Confira se não é possível identificar o papel pelo verso.',11,False),
    ('Escopo e créditos',14,True),('Este pacote contém cartas, não um manual completo. A tradução segue esta edição comunitária do projeto drFerg/2R1B_PnP; papéis avançados podem exigir regras adicionais. O Apostador deve anunciar seu palpite antes da última rodada.',11,False),
    ('Fonte: github.com/drFerg/2R1B_PnP. Créditos e referências originais preservados no repositório Ticgabriel/Financiamento. Os versos desta revisão são uniformes, sem nome, equipe ou numeração que revelem a frente.',10,False)]
    for text,size,bold in lines:
        y=paragraph(c,text,18*mm,y,174*mm,size,size*1.3,bold)-5*mm
    assert y>15*mm,y
    c.save()

def main():
    groups=cards()
    full=[g[i:i+8] for g in groups for i in range(0,len(g),8)]
    kit=groups[0]+groups[1][:2]+[next(c for c in groups[2] if c['name']=='Apostador')]
    assert len(kit)==11
    assert sum(c['team']=='red' for c in kit)==5 and sum(c['team']=='blue' for c in kit)==5
    layouts={
        'Kit_11_Jogadores_PTBR_R02.pdf':deck_pdf('Kit_11_Jogadores_PTBR_R02.pdf',[kit[:8],kit[8:]]),
        'Cartas_Completas_PTBR_R02.pdf':deck_pdf('Cartas_Completas_PTBR_R02.pdf',full)}
    guide()
    for name,layout in layouts.items():
        for sheet in layout:
            for item in sheet['cards']:
                fx,fy,w,h=item['front_mm']; bx,by,_,_=item['back_mm']
                assert abs(297-fx-w-bx)<1e-8 and fy==by
    (OUT/'Verificacao_Impressao_R02.json').write_text(json.dumps({'page_size_mm':[297,210],'card_size_mm':[60,90],'flip':'short-edge','layouts':layouts},ensure_ascii=False,indent=2)+'\n')
    (OUT/'LEIA_PRIMEIRO.txt').write_text('A4 paisagem; escala 100%; duplex com virada na borda curta. Teste as páginas 1 e 2 antes do restante. Leia o Guia_Impressao_PTBR_R02.pdf.\nKit: 2 folhas / 11 cartas. Completo: 11 folhas / 80 cartas.\n')
    members=sorted(OUT.glob('*'))
    with zipfile.ZipFile(OUT/'Two_Rooms_PTBR_Impressao_R02.zip','w',zipfile.ZIP_DEFLATED) as z:
        for f in members:
            if f.suffix!='.zip':z.write(f,f.name)
    print(json.dumps({'files':[{'name':f.name,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(OUT.glob('*'))]},indent=2))

if __name__=='__main__':main()
