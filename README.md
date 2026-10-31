# Two Rooms and a Boom — PT-BR

Adaptação comunitária do projeto [drFerg/2R1B_PnP](https://github.com/drFerg/2R1B_PnP).

## Etapas concluídas

1. **Arquivos-fonte originais:** 11 arquivos preservados em [`original/`](original/), com hashes registrados em [`ORIGEM.json`](ORIGEM.json).
2. **Tradução PT-BR:** 80 cartas em [`pt-BR/src/`](pt-BR/src/), glossário, inventário dos nomes e script de compilação. Os cinco conjuntos foram compilados e as 11 páginas de frentes foram inspecionadas. Veja as [instruções](pt-BR/README.md) e o [registro de verificação](pt-BR/VERIFICACAO.md).

3. **PDFs duplex preparados e conferidos:** gerador em [`pt-BR/gerar_impressao.py`](pt-BR/gerar_impressao.py), [instruções e verificação](pt-BR/IMPRIMIR.md). Kit de 11 jogadores em 2 folhas e conjunto completo em 11 folhas. O novo layout usa fundo claro, versos uniformes e marcas de corte.

## Kit para exatamente 14 jogadores

- [Pacote completo ZIP](pt-BR/impressao/kit_14/Pacote_14_Jogadores_PTBR.zip)
- [Cartas para imprimir inteiro - 2 folhas duplex](pt-BR/impressao/kit_14/IMPRIMIR_Cartas_14_Jogadores_PTBR.pdf)
- [Manual resumido do modo básico - 1 página](pt-BR/impressao/kit_14/MANUAL_Basico_14_Jogadores_PTBR.pdf)

Use todas as 14 cartas: Presidente + 6 azuis comuns + Bombista + 6 vermelhas comuns. Não há Apostador. Imprima as cartas em A4 paisagem, 100%, duplex, virada na borda curta; teste uma folha primeiro. O manual deve ser impresso separadamente em A4 retrato.

Os PDFs foram renderizados e conferidos, as contagens dos papéis e as coordenadas dos versos foram verificadas. As regras básicas foram conferidas no [livro de regras](https://www.playkaboom.com/TwoRooms_Rulebook_v3.pdf). O manual é um resumo independente do modo básico, não uma tradução integral do manual oficial. Para regenerar: `python3 pt-BR/gerar_kit_14.py` (requer reportlab).

## Kit exato para 6 a 12 jogadores

- [Baixar o pacote ZIP](pt-BR/impressao/kit_ate_12/Pacote_Exato_Ate_12_Jogadores_PTBR.zip)
- [PDF de cartas para imprimir inteiro](pt-BR/impressao/kit_ate_12/IMPRIMIR_Cartas_Ate_12_PTBR.pdf)
- [Guia e tabela de composição por quantidade de jogadores](pt-BR/impressao/kit_ate_12/LEIA_PRIMEIRO_Kit_Ate_12.pdf)

**Imprima somente o PDF de cartas deste kit: 4 páginas = 2 folhas duplex.** A4 paisagem, escala 100%, virada na borda curta. Teste as páginas 1 e 2 primeiro. O guia é A4 retrato e sua impressão é opcional e separada.

O kit contém 13 cartas físicas para permitir variar a quantidade de jogadores. Para 12 pessoas, use Presidente + 5 azuis comuns + Bombista + 5 vermelhas comuns e guarde o Apostador. Para as outras quantidades, siga a tabela do guia e guarde as cartas restantes antes de embaralhar.

Este kit substitui a combinação do kit antigo de 11 jogadores com páginas extras do conjunto completo.

## Outros PDFs prontos para imprimir

Os arquivos estão em [`pt-BR/impressao/`](pt-BR/impressao/):

- [Kit de 11 jogadores - 2 folhas duplex](pt-BR/impressao/Kit_11_Jogadores_PTBR_R02.pdf)
- [80 cartas - 11 folhas duplex](pt-BR/impressao/Cartas_Completas_PTBR_R02.pdf)
- [Guia de impressão](pt-BR/impressao/Guia_Impressao_PTBR_R02.pdf)
- [Pacote completo ZIP](pt-BR/impressao/Two_Rooms_PTBR_Impressao_R02.zip)

No visualizador do GitHub, use **Download raw file** para salvar o PDF. Para até 12 pessoas, prefira o kit exato acima, que já reúne as cartas necessárias em duas folhas.

**Cartas: A4 paisagem, escala 100%, duplex com virada na borda curta.** Teste as páginas 1 e 2 primeiro. O guia é A4 retrato e deve ser impresso separadamente.

Os sete binários da edição original em inglês continuam pendentes de cópia. Os PDFs PT-BR estão publicados e prontos para download.

## Origem e créditos

Árvore-fonte: `131be78a5f46beab52e953db2517ef0529987616` de [drFerg/2R1B_PnP](https://github.com/drFerg/2R1B_PnP). Créditos de design e referências no [README original](original/README.MD).

Não há arquivo de licença explícito na árvore original consultada. Esta adaptação preserva os créditos e não atribui uma licença nova aos materiais de terceiros.
