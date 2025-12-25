"""
Desafio 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.

Também poderiamos: 
numeros = (int(input()), ...)
Porém, para treino e fins de explorar a linguagem optei por este outro método.
"""
n1 = n2 = n3 = n4 = None
# Declaro as variáveis como PlaceHolder
for i in range(1, 5):
    globals()[f'n{i}'] = int(input(f'Digite o {i}° número: '))
    # Uso um loop para atribuir valores a variáveis globais através da função built-in globals()
    # Podemos usar isso para criar também, mesmo não sendo prático
    # Para este tipo de uso o correto seria uma lista
    # Estrutura usada para testes e fins de conhecimento

numeros = (n1, n2, n3, n4) # Atribuição a um indice

print(f'Foram digitados {numeros.count(9)} números 9')
if 3 in numeros:
    print(f'O primeiro número 3 foi digitado na posição {numeros.index(3)+1}')
else:
    print('Não há nenhum número 3')
for i in numeros:
    if i % 2 == 0:
        print(f'O número {i} é par')
