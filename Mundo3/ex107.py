"""
Desafio 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe 
esse módulo e use algumas dessas funções.

Para fins didáticos optei por usar POO nos EX 107 até 112.
A inspiração para isso foi:
1 - Comprimir tudo no arquivo Aula22a.py
obs: Em sistemas reais isso deve ser evitado
2 - Isso permite modularizar sem ficar muito confuso e ter várias funções soltas
3 - O arquivo pode possuir uma classe que contem as funções/métodos
respectivos a cada exercicio.
"""

from aula22a import Moeda
real = 10.5

print(real)
print(Moeda.aumentar(real, 10))
real = Moeda.diminuir(real, 10)
print(real)
print(Moeda.dobro(real))
print(Moeda.metade(real))
