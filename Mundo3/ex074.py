"""
Desafio 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor 
e o maior valor que estão na tupla.
"""

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os números em ordem de geração são: ')
for i in numeros:
    print(f'{i} ', end='')
print()

print(f'O menor número é {min(numeros)} e o maior é {max(numeros)}')
# Ou, com sorted:
print(f'O menor número é {sorted(numeros)[0]} e o maior é {sorted(numeros)[4]}')
