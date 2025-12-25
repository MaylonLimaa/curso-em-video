"""
Desafio 105: Faça um programa que tenha uma função notas() que pode receber várias notas 
de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
"""

def notas(*n, sit=False):
    notas = list()
    notas = n[:]
    media = sum(notas) / len(notas)

    relatorio = {
        'Total': len(notas),
        'Maior': max(notas),
        'Menor': min(notas),
        'Media': media
    }
    if sit:
        if media < 6:
            relatorio['Situacao'] = 'Ruim'
        elif media < 7:
            relatorio['Situacao'] = 'Bom'
        else:
            relatorio['Situacao'] = 'Ótimo'

    return relatorio

teste = notas(8, 4, 5, 8, 9, sit=True)
print(teste)
