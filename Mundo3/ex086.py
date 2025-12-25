"""
Desafio 86: Crie um programa que declare uma matriz de dimensão 3x3 
e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, 
com a formatação correta.
"""

numeros = [[], [], []]

for i in range(0, 3):
    for n in range(0,3):
        numeros[i].append(int(input('Digite um valor: ')))

for i in numeros:
    for n in i:
        print(n, end=' ')
    print()