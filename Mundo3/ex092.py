"""
Desafio 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
# Calcula idade baseada no ano atual do sistema
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))

    # Cálculo: Contratação + 35 anos de contribuição
    ano_aposentadoria = dados['contratacao'] + 35
    dados['aposentadoria'] = ano_aposentadoria - nascimento

print('-=' * 15)
# Exibição bonita usando o .items()
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
