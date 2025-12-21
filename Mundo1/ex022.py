"""
Desafio 22: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas. 
- Quantas letras ao todo (sem considerar espaços). 
- Quantas letras tem o primeiro nome.
"""

nome = input('Digite um nome: ')
contprimnome = nome.split()

print(f'O nome digitado é {nome}')
print(f'O nome em maisculo é {nome.upper()} e em minúscula é {nome.lower()}')
print(f'O nome possui {len(nome.replace(' ', ''))} letras sem considerar espaços')
print(f'O primeiro nome possui {len(contprimnome[0])} letras')
