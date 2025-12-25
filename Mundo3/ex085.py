"""
Desafio 85: Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma única lista que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
"""

numeros = [[], []]

for i in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        print('O número é par!')
        numeros[0].append(n)
    else:
        print('O número é impar!')
        numeros[1].append(n)

numeros[0].sort()
numeros[1].sort()

print(numeros)
