"""
Desafio 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

cont = 0

for i in range(0, 7):
    nasc = int(input('Digite a data de nascimento: '))
    idade = date.today().year - nasc
    if idade < 18:
        cont += 1

print(f'Temos {cont} pessoas menores de idade e {7-cont} pessoas maiores de idade')
