
"""
Desafio 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o 
recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 and r2 == r3:
        print('É um triangulo equilátero')
    elif (r1 == r2 or r2 == r3) and (r1 != r2 != r3 != r1):
        print('É um triangulo isósceles')
    else:
        print('É um triangulo escaleno')
else:
    print('Não é um triangulo')
