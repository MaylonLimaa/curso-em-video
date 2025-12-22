"""
Desafio 55: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
"""

for i in range(0, 5):
    peso = float(input('Digite o peso: '))
    if i == 0:
        maior = peso
        menor = peso
    if maior < peso:
        maior = peso
    if menor > peso:
        menor = peso

print(f'O maior peso é {maior} o menor peso é {menor}')
