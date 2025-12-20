"""
Desafio 23 - Faça um programa que leia um número de 0 a 9999.
Mostre na tela cada um dos dígitos separados.
"""
num = input('Digite um número de 0 a 9999: ')
num = ''.join(num)
cont = 0

for i in num:
    cont += 1
    print(f'O {cont}° número é {i}')
