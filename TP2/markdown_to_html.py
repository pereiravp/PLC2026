import re


def _cabecalho(match):
    nivel = len(match.group(1))
    texto = match.group(2)
    return f"<h{nivel}>{texto}</h{nivel}>"


def markdown_para_html(texto):
    texto = re.sub(r"^(#{1,3}) (.*)$", _cabecalho, texto, flags=re.MULTILINE)
    texto = re.sub(r"\*{2}(.*?)\*{2}", r"<b>\1</b>", texto)
    texto = re.sub(r"\*(.*?)\*", r"<i>\1</i>", texto)
    texto = re.sub(r"\!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', texto)
    texto = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', texto)
    texto = re.sub(r"^\d+\. (.*)$", r"<li>\1</li>", texto, flags=re.MULTILINE)
    texto = re.sub(r"(<li>.*</li>\n?)+", r"<ol>\n\g<0>\n</ol>", texto)
    return texto


if __name__ == "__main__":
    markdown = """# Exemplo

Este é um **exemplo** de texto com *itálico* e **negrito**.

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coelho.com)

1. Primeiro item
2. Segundo item
3. Terceiro item"""

    print(markdown_para_html(markdown))
