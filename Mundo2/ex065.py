"""
Desafio 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor 
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

continuar = ''
cont = 1
media = maior = menor = 0
while continuar not in 'Nn':
    num = int(input(f'Digite o {cont} número'))

    if cont == 1:
        maior = menor = num

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    media += num
    cont += 1

    continuar = input('Deseja continuar? <S/N>: ')

cont -= 1

print(f'O maior número foi {maior} e o menor {menor}')
print(f'Foram digitados {cont} números e a média entre eles foi {media/cont}')
