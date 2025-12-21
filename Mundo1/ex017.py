"""
Desafio 17: Faça um programa que calcule o cateto da hipotenusa
"""

import math

co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjascente'))
# Cateto adjascente
# h = math.sqrt(co**2 + ca**2)
h = math.hypot(co, ca)

print(f'A hipotenusa é {h}')
