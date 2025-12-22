"""
Desafio 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = str(input('Digite o sexo: '))

while sexo not in 'MF':
    sexo = input('Por gentileza, apenas F ou M:')

print('Obrigado')
