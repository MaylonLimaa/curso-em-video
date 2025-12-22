"""
Desafio 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

pt = int(input('Digite o primeito termo: '))
r = int(input('Digite a razão: '))
s = pt
i = 1

while i <= 10:
    print(f'O {i}° termo é {s}')
    i += 1
    s += r
