# Fase 3 - impressão duplex

Execute `python3 -m pip install reportlab` e depois `python3 pt-BR/gerar_impressao.py` na raiz do repositório. O gerador lê diretamente as cartas traduzidas em `pt-BR/src/` e cria os arquivos em `pt-BR/impressao/`.

- Kit de 11 jogadores: 11 cartas, 4 páginas, 2 folhas duplex; 5 vermelhas (Bombista e 4 comuns), 5 azuis (Presidente e 4 comuns) e Apostador.
- Conjunto completo: 80 cartas em 22 páginas / 11 folhas duplex, preservando as categorias e repetições da fonte.
- Guia de impressão em uma página A4 retrato; deve ser impresso separadamente das cartas.
- ZIP com os três PDFs, instruções rápidas e registro das posições para verificação.

## Configuração

Cartas: A4 paisagem, escala 100%, frente e verso, **virada na borda curta**. Não ajuste à página nem aplique espelhamento adicional. As cartas medem 60 × 90 mm, com 3 mm de espaço entre elas. Teste as páginas 1 e 2 antes de imprimir o restante.

Os versos são idênticos e não contêm identificadores de papel, equipe ou posição. Nas folhas incompletas, as posições dos versos são espelhadas horizontalmente para coincidir com as frentes após a virada na borda curta.

## Verificação

Os três PDFs foram renderizados e inspecionados. O gerador interrompe se algum texto ultrapassar a área destinada ao corpo da carta. Foram conferidas as 80 frentes e as 11 cartas do kit, as contagens de páginas e as coordenadas espelhadas dos versos. O alinhamento físico depende da impressora e requer o teste de uma folha.

O layout de impressão usa fundo claro para economizar tinta e texto escuro para melhorar a leitura. Os PDFs de teste do LaTeX da fase 2 continuam sendo apenas frentes; use o novo gerador para impressão duplex.

Os PDFs e o ZIP estão publicados em [`impressao/`](impressao/). Você pode baixá-los diretamente, sem executar o gerador. No visualizador de cada arquivo no GitHub, use Download raw file.
