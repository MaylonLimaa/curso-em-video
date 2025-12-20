"""
Desafio 26 - Faça um programa que leia uma frase pelo teclado e mostre 
quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez 
e em que posição ela aparece a última vez.
"""

frase = input('Digite uma frase: ')

print(f'A letra a aprece {frase.lower().count("a")} vezes')
print(f'Ela aparece pela primeira vez na posição {frase.lower().find('a')}')
print(f'Ela aparece pela última vez na posição {frase.lower().rfind('a')}')
