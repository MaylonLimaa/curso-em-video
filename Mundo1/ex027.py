"""
Desafio 27: Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = input('Digite um nome: ')
nome = nome.split()

print(f'O primeiro nome é {nome[0]} e o último nome é {nome[len(nome)-1]}')
