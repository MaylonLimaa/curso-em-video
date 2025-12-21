"""
Desafio 18: Faça um programa que leia um ângulo qualquer e 
mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians

ang = int(input('Digite o ângulo: '))
ang = radians(ang)
# Uso do método radians() para converter de graus para radiano

print(f'O seno é {sin(ang)}, o cosseno é {cos(ang)} e a tangente {tan(ang)}')
