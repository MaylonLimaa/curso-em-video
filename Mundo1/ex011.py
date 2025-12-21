"""
Desafio 11: Crie um programa que leia largura e altura da parede, calcule a área 
e a quantidade de tinta para pintar sabendo que cada litro de tinta pinta 2m²
"""

l = float(input('Digite a largura: '))
h = float(input('Digite a altura da parede: '))

print(f'{l} x {h} = {l*h} logo para pintar a parede é necessário {l*h/2} litros de tinta')
