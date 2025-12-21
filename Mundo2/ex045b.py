"""
Desafio 045: Crie um programa que faça o computador jogar Jokenpô com você.

Match...Case.
"""
from random import randint

JOKENPO = ('Pedra', 'Papel', 'Tesoura')
pc = JOKENPO[randint(0, 2)]

print('0 - Pedra | 1 - Papel | 2 - Tesoura')

jogador = int(input('Digite uma opção: '))

if jogador not in (0, 1, 2):
    print('Opção inválida')
    exit()

jogador = JOKENPO[jogador]

match (jogador, pc):
    # Empate: quando as duas escolhas são iguais
    # Aqui atribuimos jogador a j e p a pc
    case (j, p) if j == p:
        print('Empate')

    # Casos de derrota do jogador
    case ('Pedra', 'Papel'):
        print('Você perdeu!')
    case ('Papel', 'Tesoura'):
        print('Você perdeu!')
    case ('Tesoura', 'Pedra'):
        print('Você perdeu!')

    # Casos de vitória do jogador
    case ('Pedra', 'Tesoura'):
        print('Você venceu!')
    case ('Papel', 'Pedra'):
        print('Você venceu!')
    case ('Tesoura', 'Papel'):
        print('Você venceu!')
