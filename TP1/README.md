# TP1 - Expressão Regular que não contenham 011

## Autor

- Nome: Gonçalo Simões Pereira
- Id: A111783

<p align="center">
  <img src="../foto.jpg" alt="Foto" width="150">
</p>

## Resumo

O exercício pedia uma expressão regular que aceite strings binárias que não contenham a substring "011". A expressão construída foi 1*(0+1)*0*, considerando três blocos:

- uma sequência inicial de zero ou mais 1's;
- seguida de zero ou mais repetições de "um ou mais 0's seguidos de exatamente um 1";
- terminando com zero ou mais 0's. Desta forma, nunca é possível formar dois 1 consecutivos logo a seguir a um 0, o que garante que a substring "011" nunca ocorre.

A expressão foi validada com vários casos de teste: strings sem zeros, com o padrão proibido no início, no meio e no fim, e a string vazia.

## Lista de resultados

[Expressão Regular] (expressao)

https://regex101.com/?regex=%5E1*%280%2B1%29*0*%24&testString=10101%0A0101%0A0110%0A0011%0A010101010000%0A1110001010%0A0001%0A101011%0A%0A01110%0A1110%0A000%0A&flags=gm&flavor=pcre2&delimiter=%2F
