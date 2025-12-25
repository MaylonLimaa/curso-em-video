"""
Desafio 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem 
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não 
formatado pela função moeda(), desenvolvida no desafio 108.

Para fins didáticos optei por usar POO nos EX 107 até 112.
A inspiração para isso foi:
1 - Comprimir tudo no arquivo Aula22a.py
obs: Em sistemas reais isso deve ser evitado
2 - Isso permite modularizar sem ficar muito confuso e ter várias funções soltas
3 - O arquivo pode possuir uma classe que contem as funções/métodos
respectivos a cada exercicio.
"""
from aula22a import Moeda

real = 1.68

print(Moeda.dobro(real, True))
print(Moeda.dobro(real))