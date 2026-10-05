# TP2

## Autor

- Nome: Gonçalo Simões Pereira
- Id: A111783

<p align="center">
  <img src="../foto.jpg" alt="Foto" width="150">
</p>

## Resumo

O exercício pedia um conversor de Markdown para HTML em Python, para os seguintes elementos: cabeçalhos (#, ## e ###), negrito (**texto**), itálico (*texto*), lista numerada, link e imagem. Para cada elemento foi construída uma expressão regular com grupos de captura, aplicada com `re.sub` para substituir a sintaxe Markdown pela tag HTML correspondente.

A ordem de aplicação das expressões foi importante em dois casos: o negrito tem de ser convertido antes do itálico, pois ambos usam o caráter `*` e uma conversão na ordem errada deixaria asteriscos por trocar; a imagem tem de ser convertida antes do link, pois a sintaxe da imagem (`![texto](url)`) contém a sintaxe do link lá dentro. A lista numerada foi tratada em dois passos: primeiro cada linha `N. texto` é convertida em `<li>texto</li>`, depois o bloco de `<li>` consecutivos é envolvido por `<ol>` e `</ol>`.

A função foi validada com um texto que combina todos os elementos ao mesmo tempo, confirmando que as conversões não interferem umas com as outras.

## Lista de resultados

- [Conversor de Markdown para HTML](markdown_to_html.py)
