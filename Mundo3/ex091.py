"""
Desafio 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint

jogadores = {
    'Pedro': {'nome': 'Pedro',
     'resultado': randint(1, 6)},
    'Davi': {'nome': 'Davi',
              'resultado': randint(1, 6)},
    'Ana': {'nome': 'Ana',
     'resultado': randint(1, 6)},
    'Robson': {'nome': 'Robson',
              'resultado': randint(1, 6)}
}
resultado = [jogador['resultado']  for jogador in jogadores.values()]
resultado_ordenado = sorted(resultado, reverse=True)
jogadores_ordenados = sorted(jogadores.values(), key=lambda x: x['resultado'], reverse=True)

for jogador in jogadores_ordenados:
    print(f"{jogador['nome']} -> {jogador['resultado']}")
