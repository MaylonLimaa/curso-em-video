"""
Desafio 101: Crie um programa que tenha uma função chamada voto() que vai receber 
como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
from datetime import date
def voto(nasc):
    idade = date.today().year - nasc
    if idade >= 18:
        return 'Obrigatório'
    elif idade >= 16:
        return 'Opcional'
    else:
        return 'Negado'

print(voto(2000))
print(voto(2008))
print(voto(2012))
