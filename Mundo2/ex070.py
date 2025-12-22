"""
Desafio 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

total = prods = barato = 0
nomebarato = ''

while True:
    nome = input('Qual o produto? ')
    preco = float(input('Qual seu preço? '))

    if barato == 0:
        barato = preco
        nomebarato = nome
    if barato > preco:
        barato = preco
        nomebarato = nome

    if preco > 1000:
        prods += 1
    
    total += preco

    continuar = input('Deseja continuar? <S/N> ')
    if continuar == 'n':
        break

print(f'O produto mais barato foi {nomebarato} e houveram {prods} produtos acima de R$ 1000')
print(f'O valor total foi de R$ {total}')
