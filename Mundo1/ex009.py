"""
Desafio 9 - Faça um programa que leia um número e mostre sua tabuada.
Requisitos - Aula 7

Para fins de praticidade e devido a prévio conhecimento, foi utilizado o loop for.
"""

n = int(input('Digite um número: '))

print(f'{"="*15} Tabuada {"="*15}')
# Print de formatação que exibe tabuada centralizado com 15 simbolos = para cada lado
for i in range (1, 11):
    # Loop de repetição de 1 até 10
    print(f'{" "*10} {n} x {i} = {n*i}')
    # Exibe o resultado formatado em cada um dos loops
