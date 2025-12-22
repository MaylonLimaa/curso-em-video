"""
Desafio 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
"""
pt = int(input('Digite o primeito termo: '))
r = int(input('Digite a razão: '))
s = pt + r
for i in range(0, 10):
    print(f'O termo {i+1} é {s}')
    s += r
