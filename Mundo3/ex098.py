"""
Desafio 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
A) de 1 até 10, de 1 em 1
B) de 10 até 0, de 2 em 2
C) uma contagem personalizada
"""

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim:
        if passo > 0:
            passo *= -1
        for i in range(inicio, fim-1, passo):
            print(i)
            sleep(1)
    else:
        for i in range(inicio, fim+1, passo):
            print(i)
            sleep(1)


contador(1, 10, 1)
contador(10, 0, 2)
contador(5, 2, 1)
