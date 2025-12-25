
"""
Desafio 87: Melhore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
numeros = [[], [], []]
spar = scol = mlin = 0

for i in range(0, 3):
    for n in range(0,3):
        numeros[i].append(int(input('Digite um valor: ')))

for i in numeros:
    for n in i:
        print(n, end=' ')
        if n % 2 == 0:
            spar += n
    print('---------------')

for i in range(0, 3):
    scol += numeros[i][2]
for i in range(0, 3):
    if mlin == 0:
        mlin = numeros[1][i]
    if mlin < numeros[1][i]:
        mlin = numeros[1][i]

print(f'A soma dos pares é {spar} e o maior valor da segunda linha é {mlin}')
print(f'Enquanto a soma da terceira coluna é {scol}')
