"""
Desafio 045: Crie um programa que faça o computador jogar Jokenpô com você.

ifs, elifs e else.
"""

from random import randint

JOKENPO = ('Pedra', 'Papel', 'Tesoura')
pc = JOKENPO[randint(0, 2)]
jogador = int()

print('0 - Pedra | 1 - Papel | 2 - Tesoura')
jogador = int(input('Digite uma opção: '))
if jogador not in (0, 1, 2):
    print('Opção inválida')
    exit()
jogador = JOKENPO[jogador]

if jogador == pc:
    print('Empate')
else:
    if jogador == JOKENPO[0] and pc == JOKENPO[1]:
        print('Você perdeu!')
    elif jogador == JOKENPO[0] and pc == JOKENPO[2]:
        print('Você venceu!')
    elif jogador == JOKENPO[1] and pc == JOKENPO[0]:
        print('Você venceu!')    
    elif jogador == JOKENPO[1] and pc == JOKENPO[2]:
        print('Você perdeu!')
    elif jogador == JOKENPO[2] and pc == JOKENPO[0]:
        print('Você perdeu!')
    elif jogador == JOKENPO[2] and pc == JOKENPO[1]:
        print('Você venceu!')
