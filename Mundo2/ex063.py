
"""
Desafio 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela 
os N primeiros elementos de uma Sequência de Fibonacci. 
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

num = int(input('Quantos elementos deve ter a sequência? '))
cont = 0
t1 = 0
t2 = 1

while cont <= num:
    t3 = t1 + t2
    print(f'->{t3}',end='')
    t1 = t2
    t2 = t3
    cont += 1
