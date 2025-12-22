"""
Desafio 68: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias 
consecutivas que ele conquistou no final do jogo.
"""

from random import randint

vit = 0

while True:
    jgd = input('Escolha par ou impar: ').strip().lower()
    if jgd == 'par':
        jgd = 0
        pc = 1
    else:
        jgd = 1
        pc = 0
    
    pcnum = randint(0, 5)
    jgdnum = int(input('Digite um número de 0 a 5: '))

    if (pcnum+jgdnum) % 2 == 0:
        if jgd == 0:
            print('Parabéns você venceu')
            vit += 1
        else:
            print('Você perdeu!')
            break
    else:
        if jgd == 1:
            print('Parabéns você venceu')
            vit += 1
        else:
            print('Você perdeu!')
            break
