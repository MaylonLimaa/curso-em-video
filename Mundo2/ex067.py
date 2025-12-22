"""
Desafio 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número 
solicitado for negativo.
"""

while True:
    num = int(input('Digite um número: '))
    if num < 0:
        print('Número negativo!')
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
