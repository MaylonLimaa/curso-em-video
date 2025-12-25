"""
Desafio 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que sejam monetários.

Para fins didáticos optei por usar POO nos EX 107 até 112.
A inspiração para isso foi:
1 - Comprimir tudo no arquivo Aula22a.py
obs: Em sistemas reais isso deve ser evitado
2 - Isso permite modularizar sem ficar muito confuso e ter várias funções soltas
3 - O arquivo pode possuir uma classe que contem as funções/métodos
respectivos a cada exercicio.
"""
from utilidadesCeV import dado, moeda

num = dado.leiaDinheiro('Digite um valor ')
num = moeda.Moeda.aumentar(num, 25)
print(moeda.Moeda.moeda(num))