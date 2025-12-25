"""
Desafio 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoa = []
pesados = []
leves = []
maior = menor = 0
while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso'))
    if not pessoa:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    pessoa.append([nome, peso])
    resp = input('Deseja continuar? <S/N> ')
    if resp == 'n':
        break

for i in pessoa:
    if maior == i[1]:
        pesados.append(i)
    if menor == i[1]:
        leves.append(i)

print(f'Foram cadastradas {len(pessoa)} pessoas')
print(f'As pessoas mais leves são {leves}')
print(f'As Pessoas mais pesadas sao {pesados}')
