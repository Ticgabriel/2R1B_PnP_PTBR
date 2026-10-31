#!/usr/bin/env python3
"""Kit básico para exatamente 14 jogadores. Requer reportlab e gerar_impressao.py."""
from pathlib import Path
import importlib.util, zipfile
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('impressao',ROOT/'gerar_impressao.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
OUT=ROOT/'impressao'/'kit_14';OUT.mkdir(parents=True,exist_ok=True);g.OUT=OUT
groups=g.cards()
red=next(c for c in groups[0] if c['team']=='red')
blue=next(c for c in groups[0] if c['team']=='blue')
bomber=next(c for c in groups[1] if c['name']=='Bombista')
president=next(c for c in groups[1] if c['name']=='Presidente')
deck=[president,bomber]+[card for _ in range(6) for card in (blue,red)]
assert len(deck)==14 and sum(c['team']=='blue' for c in deck)==7 and sum(c['team']=='red' for c in deck)==7
layout=g.deck_pdf('IMPRIMIR_Cartas_14_Jogadores_PTBR.pdf',[deck[:8],deck[8:]])
for sheet in layout:
 for card in sheet['cards']:
  x,y,w,h=card['front_mm'];bx,by,_,_=card['back_mm']
  assert abs(297-x-w-bx)<1e-8 and y==by

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Body14',fontName='Helvetica',fontSize=10.3,leading=14,spaceAfter=8))
styles['Title'].fontSize=21
P=lambda s:Paragraph(s,styles['Body14'])
items=[Paragraph('Duas salas e uma bomba',styles['Title']),P('<b>Kit para 14 jogadores | Manual resumido do modo básico</b>'),
Paragraph('1. O que imprimir',styles['Heading2']),
P('Imprima <b>IMPRIMIR_Cartas_14_Jogadores_PTBR.pdf inteiro</b>: 4 páginas, equivalentes a <b>2 folhas duplex</b>. A4 paisagem, escala 100% / tamanho real, virada na <b>borda curta</b>. Desative ajustar à página. Teste as páginas 1 e 2 e confira contra a luz antes da segunda folha. Recorte pelas marcas; cartas de 60 × 90 mm.'),
P('Este manual é A4 retrato: imprima separadamente, se quiser. O ZIP contém exatamente os dois PDFs e as instruções rápidas. Não precisa combinar com arquivos anteriores.'),
Paragraph('2. Preparação e objetivo',styles['Heading2']),
P('Use Presidente + 6 azuis e Bombista + 6 vermelhas. Embaralhe, distribua uma carta por pessoa e forme duas salas aleatórias de sete. Olhem suas cartas ao iniciar. Separe um cronômetro e dois objetos para identificar líderes.'),
P('Após a última troca, Bombista e Presidente juntos: Vermelhos vencem; separados: Azuis vencem. Não há Apostador neste kit.'),
Paragraph('3. Conversa e liderança',styles['Heading2']),
P('Permaneçam na sala, sem comunicação entre salas. Podem mentir e mostrar a carta inteira voluntariamente; não troquem papéis. Neste modo básico, não mostrem somente a cor.'),
P('O primeiro líder é indicado por outra pessoa. Pode ceder o posto a alguém que aceite, sem recebê-lo de volta na mesma rodada. Mais da metade da sala pode apoiar outro líder. O líder não pode ser refém.'),
Paragraph('4. Rodadas e trocas',styles['Heading2'])]
table=Table([['Rodada','Duração','Cada sala envia'],['1','3 minutos','2 reféns'],['2','2 minutos','1 refém'],['3','1 minuto','1 refém']],colWidths=[35*mm,55*mm,80*mm],rowHeights=[9*mm]*4)
table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#153f8f')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTNAME',(0,1),(-1,-1),'Helvetica'),('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#eff5ff'),colors.white]),('GRID',(0,0),(-1,-1),.25,colors.HexColor('#cbd5e1'))]))
items.extend([table,Spacer(1,3*mm),P('Ao terminar o tempo, cada líder fixa os reféns, sem alterar a escolha. Líderes se encontram sem reféns; iniciam o próximo cronômetro, salvo após a última rodada, e chamam os escolhidos para trocar de sala. Líderes retornam. Após a terceira troca, todos revelam as cartas e verificam o resultado.'),
Paragraph('5. Antes de começar',styles['Heading2']),
P('Escolham um sinal sonoro audível nas duas salas. Deixem o caminho livre para as trocas. Se faltarem pessoas, não retirem cartas ao acaso: este pacote foi montado para exatamente 14.'),
P('<b>Escopo:</b> este resumo cobre o modo básico deste kit. Não inclui personagens especiais, carta enterrada nem o modo avançado de cinco rodadas.'),
P('<b>Fontes e créditos:</b> jogo de Alan Gerding e Sean McCoy / Tuesday Knight Games. Regras: <link href="https://www.playkaboom.com/TwoRooms_Rulebook_v3.pdf" color="blue">playkaboom.com/TwoRooms_Rulebook_v3.pdf</link>, pp. 3-10. Cartas: drFerg/2R1B_PnP; tradução e layout: Ticgabriel/2R1B_PnP_PTBR. Resumo independente, não manual oficial.')])
SimpleDocTemplate(str(OUT/'MANUAL_Basico_14_Jogadores_PTBR.pdf'),pagesize=(210*mm,297*mm),rightMargin=20*mm,leftMargin=20*mm,topMargin=13*mm,bottomMargin=13*mm,title='Manual básico para 14 jogadores').build(items)
(OUT/'LEIA_PRIMEIRO.txt').write_text('KIT PARA EXATAMENTE 14 JOGADORES\n\nImprima IMPRIMIR_Cartas_14_Jogadores_PTBR.pdf inteiro: 4 páginas = 2 folhas duplex.\nA4 paisagem, 100%, borda curta. Teste páginas 1 e 2 primeiro.\n14 cartas: Presidente + 6 azuis comuns + Bombista + 6 vermelhas comuns. Sem Apostador.\nO manual é A4 retrato; sua impressão é separada e opcional.\nModo básico: 3, 2 e 1 minutos; cada sala envia 2, 1 e 1 reféns, respectivamente.\n')
with zipfile.ZipFile(OUT/'Pacote_14_Jogadores_PTBR.zip','w',zipfile.ZIP_DEFLATED) as z:
 for name in ['IMPRIMIR_Cartas_14_Jogadores_PTBR.pdf','MANUAL_Basico_14_Jogadores_PTBR.pdf','LEIA_PRIMEIRO.txt']:
  z.write(OUT/name,name)
print(OUT)
