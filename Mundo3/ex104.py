"""
Desafio 104: Crie um programa que tenha uma função chamada leiaInt(), que vai funcionar 
de forma semelhante à função input() do Python, só que fazendo a validação 
para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
"""

def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            return num
        print('Por gentileza, apenas números.')

n = leiaInt('Digite um valor ')
print(n)
