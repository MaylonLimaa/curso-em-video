"""
Desafio 108: Adapte o código do desafio 107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.

Para fins didáticos optei por usar POO nos EX 107 até 112.
A inspiração para isso foi:
1 - Comprimir tudo no arquivo Aula22a.py
obs: Em sistemas reais isso deve ser evitado
2 - Isso permite modularizar sem ficar muito confuso e ter várias funções soltas
3 - O arquivo pode possuir uma classe que contem as funções/métodos
respectivos a cada exercicio.
"""
from aula22a import Moeda
real = 10.559746458
print(Moeda.moeda(real))
