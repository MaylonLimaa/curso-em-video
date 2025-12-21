
"""
Desafio 037: Escreva um programa que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

num = int(input('Digite um número: '))
print('='*60)
print(' '*5, '1 - Binário | 2 - Octal | 3 - Hexadecimal', ' '*5)
print('='*60)
opcao = int(input('Digite a opção: '))
if opcao == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida!')
