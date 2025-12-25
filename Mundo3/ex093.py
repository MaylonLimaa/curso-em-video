"""
Desafio 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, 
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()
partidas = list()

# 1. Coleta de dados básicos
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# 2. Coleta de gols por partida
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))

# 3. Guardando a lista e o total no dicionário
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)

# 4. Exibição organizada (Opcional, mas recomendado)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
