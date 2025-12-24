"""
Desafio 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

numeros = list()
qtd = int(input('Quantos números deseja adicionar? '))

for i in range(1, qtd+1):
    numeros.append(float(input(f'Digite o {i}° número: ')))

print(f'O menor número foi {min(numeros)} a posição dele é {numeros.index(min(numeros))+1}')
print(f'O maior número foi {max(numeros)} a posição dele é {numeros.index(max(numeros))+1}')
