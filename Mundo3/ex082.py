"""
Desafio 82: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares 
e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
"""

pares = []
impares = []
numeros =[]

while True:
    numeros.append(float(input('Digite o número: ')))
    print('Deseja continuar?')
    teste = input('<S/N> : ')
    if 'Nn' in teste:
        break

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(numeros)
print(pares)
print(impares)
