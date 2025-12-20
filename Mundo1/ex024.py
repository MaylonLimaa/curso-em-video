""" 
Desafio 24 - Crie um programa que leia o nome de uma cidade diga 
se ela começa ou não com o nome "SANTO".
"""

cidade = input('Digite o nome da cidade: ')
cidade = cidade.strip()

if 'Santo' in cidade and 'S' == cidade[0]:
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')