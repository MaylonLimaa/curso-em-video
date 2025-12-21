"""
Desafio 4: Crie um programa que leia algo pelo teclado e faça a identificação de seus dados
"""

vlr = input('Digite alguma informação: ')

print(f'O valor é alpha númerico: {vlr.isalnum()}')
print(f'O valor é composto apenas de letras: {vlr.isalpha()}')
print(f'O valor está em minúsculo: {vlr.islower()}')
print(f'O valor é composto apenas de números: {vlr.isnumeric()}')
print(f'O valor está maiscúlo: {vlr.isupper()}')
print(f'O valor está capitalizado: {vlr.istitle()}')
print(f'O valor tem apenas espaços: {vlr.isspace}')
