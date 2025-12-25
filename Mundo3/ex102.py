"""
Desafio 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(num, show=False):
    f1 = num - 1
    resultfat = num

    if show:
        print(f'{num}! = {resultfat}x{f1}', end='')
        while True:
            if f1 == 1:
                break
            resultfat *= f1
            f1 -= 1
            print(f'x{f1}', end='')
        print(f'= {resultfat}')
    else:
        while True:
            if f1 == 1:
                break
            resultfat *= f1
            f1 -= 1
        return resultfat

fatorial(5, True)
print(fatorial(5))


