
"""
Desafio 97: Faça um programa que tenha uma função chamada escreva(), que receba um texto 
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""

def escreva(texto):
    print('~'*len(texto))
    print(texto)
    print('~'*len(texto))

escreva('Olá, mundo!')
escreva('Três pratos de trigo para três tigres tristes')
