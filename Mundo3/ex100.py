"""
Desafio 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() 
e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint

def sorteia(n):
    for i in range(0, 5):
        n.append(randint(0, 100))
    print(f'Os números sorteados foram: {n}')

def somaPar(n):
    spar = 0
    for i in n:
        if i % 2 == 0:
            spar += i
    print(f'A soma dos números pares é {spar}')

numeros = []
sorteia(numeros)
somaPar(numeros)
