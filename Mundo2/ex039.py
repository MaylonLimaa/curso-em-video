
"""
Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e 
nforme, de acordo com sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar 
ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

nasc = int(input('Em que ano nasceu? '))
idade = date.today().year - nasc
if idade == 18:
    print('Você está na idade de se alistar!')
elif idade < 18:
    print('Você ainda não está na idade de se alistar!')
    print(f'Precisa se alistar em {18 - idade}')
else: 
    print(f'Você passou do prazo! era para se alistar há {idade - 18} anos')
