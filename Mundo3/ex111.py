"""
Desafio 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados 
moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 
para o primeiro pacote e mantenha tudo funcionando.

Para fins didáticos optei por usar POO nos EX 107 até 112.
A inspiração para isso foi:
1 - Comprimir tudo no arquivo Aula22a.py
obs: Em sistemas reais isso deve ser evitado
2 - Isso permite modularizar sem ficar muito confuso e ter várias funções soltas
3 - O arquivo pode possuir uma classe que contem as funções/métodos
respectivos a cada exercicio.
"""

from utilidadesCeV import moeda

real = 5.6089

print(moeda.Moeda.aumentar(real, 10, True))
