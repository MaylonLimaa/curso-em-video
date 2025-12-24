"""
Desafio 79: Crie um programa onde o usuário possa digitar vários valores numéricos 
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

Optei por usar set pois ele não é abordado no curso. A solução comum esperada:
if num not in numeros:
    numeros.append(num)
"""

numeros = set()
qtd = int(input('Quantos números deseja adicionar? '))
print('Números repetidos serão ignorados.')

for i in range(1, qtd+1):
    numeros.add(float(input(f'Digite o {i}° número: ')))

numeros = list(numeros)
numeros.sort()
for i, vlr in enumerate(numeros):
    print(f'O {i+1}° número é {vlr}')
