"""
Desafio 81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

numeros = list()
while True:
    numeros.append(float(input('Digite o número: ')))
    print('Deseja continuar?')
    teste = input('<S/N> : ')
    if 'Nn' in teste:
        break

print(sorted(numeros, reverse=True))
print(f'Foram digitados {len(numeros)} números')
if 5 in numeros:
    print('5 está na lista')
else:
    print('5 não está na lista')
