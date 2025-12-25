"""
Desafio 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo 
em uma lista composta. No final, mostre um boletim contendo a média de cada um 
e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    # Adicionamos uma lista composta: [Nome, [Lista de Notas], Média]
    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar? [S/N] ')).strip().lower()
    if resp == 'n':
        break

print('-=' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for i, aluno in enumerate(ficha):
    # aluno[0] é o nome, aluno[2] é a média
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if opc == 999:
        print('FINALIZANDO...')
        break

    # Verifica se o índice digitado existe na lista
    if opc <= len(ficha) - 1:
        # ficha[opc][0] é o nome, ficha[opc][1] é a sublista de notas
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    else:
        print('Aluno não encontrado! Tente novamente.')
