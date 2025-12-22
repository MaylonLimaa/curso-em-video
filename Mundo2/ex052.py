"""
Desafio 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

n = int(input('Digite um número: '))
tentativa = True
for i in range(2, n):
    if n % i == 0:
        print('Não é primo')
        tentativa = False
        break

if tentativa:
    print(f'O número {n} é primo')
