"""
Curso Python #08 - Utilizando Módulos

Há duas formas de usar módulos/pacotes em python.
A primeira é importando tudo, usando, por exemplo, apenas import
A segunda é importando apenas oque deseja, usando from import
Exemplo prático:
import math
Importamos tudo que math possui
from math import sqrt
importamos apenas o método/função sqrt
"""

import math
# Importa TUDO de math
from random import random, randint
# Importa random de random

print(math.sqrt(5))
# Raiz quadrada usando math.sqrt()

raiz = math.sqrt(5)
# Variável recebe a raiz

print(f'A raiz quadrada de 5 é : {math.ceil(raiz)}')
# Arredonda a maior

print(f'A raiz quadrada de 5 é : {math.floor(raiz)}')
# Arredonda a menor

print(random())
# Gera algum número aleatório entre 0 e 1

print(math.floor(random()*10))
# Desta vez multiplica o número por 10, sendo assim, gera algo entre 0 e 10 e arredonda a menor

print(randint(1, 100))
# Usa o método randint() para criar um número aleatório entre 1 e 100
