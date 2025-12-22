"""
Desafio 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem 
mais velho e quantas mulheres têm menos de 20 anos.

Para simplificação, não serão feitas tratativas de erros.
"""

cont = 0
media = 0
maisvelho = ''
idadetemp = 0

for i in range(0, 4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo <M/F>: ')
    media += idade

    if sexo == 'f' and idade < 20:
        cont += 1
    if sexo == 'm':
        if idade > idadetemp:
            idadetemp = idade
            maisvelho = nome

print(f'Temos um total de {cont} mulheres com idade inferior a 20 anos')
if maisvelho != '':
    print(f'O homem mais velho se chama {maisvelho} e tem {idadetemp} anos')
else:
    print('Não foram cadastrados homens')
print(f'A média de idade do grupo é {media/4}')
