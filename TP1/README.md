# TP1 - Expressão Regular que não contenham 011

## Autor

- Nome: Gonçalo Simões Pereira
- Id: A111783

<p align="center">
  <img src="../foto.jpg" alt="Foto" width="150">
</p>

## Resumo

## Resumo

O exercício pedia uma expressão regular que aceite strings binárias que não contenham a substring "011".
A expressão construída foi `1*(0+1)*0*`, considerando três blocos:

* uma sequência inicial de zero ou mais 1's;
* seguida de zero ou mais repetições de "um ou mais 0's seguidos de exatamente um 1";
* terminando com zero ou mais 0's. Desta forma, nunca é possível formar dois 1 consecutivos logo a seguir a um 0, o que garante que a substring "011" nunca ocorre.

A expressão foi validada com vários casos de teste: strings sem zeros, com o padrão proibido no início, no meio e no fim, e a string vazia.


## Lista de resultados

[Expressão regular](expressao.py)

https://regex101.com/r/jKN6PS/1
