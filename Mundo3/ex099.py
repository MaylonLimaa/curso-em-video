"""
Desafio 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros 
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*num):
    numeros = list(num)
    numeros_organizados = sorted(numeros, reverse=True)
    print(f'Os números foram {numeros}')
    print(f'Em ordem decrescente {numeros_organizados}')
    if not numeros:
        print('Sem números')
    else:
        print(f'E o maior foi {numeros_organizados[0]}')


maior(1, 2, 3, 5, 4, 8, 9, 10)
