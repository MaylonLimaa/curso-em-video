
"""
Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

n = int(input('Digite um número: '))
vlrinicial = n
fatorial = n

while n != 1 and n > 0:
    fatorial = fatorial * (n-1)
    n -= 1

if fatorial == 0:
    fatorial = 1

print(f'O fatorial de {vlrinicial} é {fatorial}')
