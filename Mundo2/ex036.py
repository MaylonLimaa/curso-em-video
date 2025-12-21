"""
Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

sal = float(input('Qual seu salário? '))
tempo = int(input('Em quantos anos vai pagar? '))
vlrcasa = float(input('Qual o valor da casa? '))
tempo = tempo * 12
parcelas = vlrcasa/tempo
vlraproveit = sal * 0.3

if vlraproveit >= parcelas:
    print('Parabéns, o empréstimo foi aprovado')
else:
    print('Valor negado')