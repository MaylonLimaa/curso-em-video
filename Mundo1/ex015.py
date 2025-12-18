"""
Desafio 15 - Crie um algortimo que calcule o preço de aluguel de um carro
baseado em dias e km, onde cada dia custa 60 reais e cada km 15 centavos
Requisitos: Aula 07
"""

dist = int(input('Quantos km o carro percorreu? '))
dias = int(input('Por quantos dias usou o carro? '))
valordist = dist * 0.15
valordias = dias * 60

print(f'Como o carro percorreu {dist}km e foi alugado por {dias} dias')
print(f'O valor de aluguel é de R$ {valordist + valordias}')