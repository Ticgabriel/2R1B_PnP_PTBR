# Two Rooms and a Boom — tradução PT-BR

Tradução comunitária das **80 cartas** do projeto [drFerg/2R1B_PnP](https://github.com/drFerg/2R1B_PnP), distribuídas nos mesmos cinco conjuntos do original. Os nomes e as regras seguem essa edição; não representam uma revisão conforme edições posteriores do jogo.

## Compilar

Em Linux, macOS ou WSL com pdfLaTeX e os pacotes `geometry`, `tikz`, `inputenc`, `fontenc` e `helvet`:

```bash
cd pt-BR
bash compile_all
```

O script interrompe ao encontrar erro, deixa os logs em `temp/` e gera cinco PDFs em `pdf/`. Esta fase gera **somente as frentes**, sem imposição duplex nem marcas de corte. Não use estes arquivos como pacote final de impressão. Os versos e o kit para 11 jogadores serão conferidos na fase 3.

A fonte Helvetica substitui Roboto para facilitar a compilação; as letras A e V identificam as equipes além das cores. O tamanho das cartas continua em 6 × 9 cm, em páginas A4 paisagem.

## Termos

| Original | Tradução e sentido |
| --- | --- |
| Card Share | Compartilhar a carta: dois jogadores mostram suas cartas um ao outro, em particular. |
| Colour Share | Compartilhar a cor: dois jogadores mostram apenas a cor um ao outro, em particular. |
| Public Reveal / Card Reveal | Revelar a carta em público. |
| Private Reveal | Revelar a carta em particular a outra pessoa; não implica reciprocidade, salvo quando a regra exigir. |
| Colour Reveal | Revelar a cor em público. |
| Buried card | Carta enterrada: carta separada, fora das mãos dos jogadores. |
| Dead | Morto: condição dentro do jogo. |
| Leader / hostage | Líder / refém. |
| Foolish / shy / coy / savvy | Tolo / tímido / reservado / perspicaz. |

`cartas.json` relaciona cada ocorrência de carta ao nome original e à tradução. Cartas repetidas do projeto-fonte foram preservadas, inclusive Líder Nato, Anarquista e Lacaio.

Alguns papéis avançados dependem de regras de preparação, condições ou cartas enterradas que não são explicadas integralmente nas cartas. Esta tradução não é um manual completo. Combine com o grupo o uso de papéis que envolvem contato físico.

## Créditos

Projeto-fonte e design: drFerg/2R1B_PnP e referências presentes no [README original](../original/README.MD). Os arquivos em `original/` permanecem intactos. Nenhuma licença nova é atribuída aos materiais de terceiros.
