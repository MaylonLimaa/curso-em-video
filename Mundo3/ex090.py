"""
Desafio 90: Faça um programa que leia nome e média de um aluno, guardando também a situação 
em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

nome = input('Digite o nome: ')
media = float(input('Digite a média: '))

aluno = {
    'nome': nome,
    'media': media,
    'situacao': 'Aprovado' if media >= 6 else 'Reprovado'
}

for k, v in aluno.items():
    print(f'{k}: {v}')
