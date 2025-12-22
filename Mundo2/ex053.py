"""
Desafio 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços.
"""

frase = input('Digite uma frase: ').replace(' ', '').lower()
contrario = ''

for letra in range(len(frase) -1, -1, -1):
    contrario += frase[letra]

if contrario == frase:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
