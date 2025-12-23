"""
Desafio 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela 
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
"""

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 
         'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 
         'Red Bull Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

"""
Usando for para A e B
for i in range(0, 5):
    print(f'O {i+1}° colocado é {times[i]} ', end='')
print()
for i in range(19, 16, -1):
    print(f'O {i+1}° colocado é {times[i]} ', end='')
print()
"""
# Usando slicing para A
print('Os times das primeiras cinco colocações respectivamente são: ')
print(times[:5])

#Usando slicing para B
print('Os times das últimas quatro colocações respectivamente são: ')
print(times[-4:])

print('Os times em ordem alfabética são:  ')
for i, time in enumerate(sorted(times)):
    print(f'{time},  ', end='')

if 'Chapecoense' in times:
    posicao = times.index('Chapecoense')
    print(f'O {times[posicao]} está em {posicao}° na colocação')
else:
    print('O time Chapecoense não está na tabela')
