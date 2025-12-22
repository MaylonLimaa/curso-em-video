"""
Desafio 71: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

valorsaque = int(input('Qual o valor do saque: '))
memsaque = valorsaque
cont50 = cont20 = cont10 = cont1 = 0
while True:
    while True:
        if valorsaque >= 50:
            valorsaque -= 50
            cont50 += 1
        else:
            break

    while True:
        if valorsaque >= 20:
            valorsaque -= 20
            cont20 += 1
        else:
            break

    while True:
        if valorsaque >= 10:
            valorsaque -= 10
            cont10 += 1
        else:
            break

    while True:
        if valorsaque >= 1:
            valorsaque -= 1
            cont1 += 1
        else:
            break

    if valorsaque == 0:
        break

print(f'Você sacou {memsaque}')
print(f'Você recebeu {cont50} notas de 50')
print(f'Você recebeu {cont20} notas de 20')
print(f'Você recebeu {cont10} notas de 10')
print(f'Você recebeu {cont1} notas de 1')
