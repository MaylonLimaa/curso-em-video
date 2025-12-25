"""
Desafio 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint

sorteio = []
listasorteio = []

njogos = int(input('Quantos jogos vai gerar? '))
cont =  i = 0

while cont < njogos:
    i = 0
    while i < 6:
        n = randint(1, 60)
        if n not in sorteio:
            sorteio.append(n)
            i += 1

    listasorteio.append(sorteio[:])
    sorteio.clear()
    cont += 1

print(listasorteio)
