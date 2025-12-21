
"""
Desafio 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

from datetime import date

ano = int(input('Digite o nascimento: '))
i = date.today().year - ano
if i > 25:
    print('Master')
elif i > 19:
    print('Sênior')
elif i > 14:
    print('Júnior')
elif i > 9:
    print('Infantil')
else:
    print('mirim')
