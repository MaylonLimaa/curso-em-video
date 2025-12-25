"""
Desafio 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) 
e mostrá-lo por extenso.
"""

extenso = ('Zero', 'Um', 'Dois','Três', 'Quatro', 'Cinco', 
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numeral = int(input('Digite um número entre 0 e 20: '))
while numeral < 0 or numeral > 20:
    numeral = int(input('Por gentileza, é obrigatório que seja de 0 a 20: '))

print(f'{numeral} em extenso é {extenso[numeral]}')
