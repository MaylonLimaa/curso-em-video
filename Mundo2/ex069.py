"""
Desafio 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.

Simplificação das validações de forma proposital.
"""

maiores = homens = mulheres = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo <F/M>: ').lower()

    if idade > 18:
        maiores += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres += 1
    
    continuar = input('Deseja continuar? <S/N> ')
    if continuar == 'n':
        break

print(f'Há um total de {maiores} pessoas maiores de 18 anos')
print(f'Foram cadastrados {homens} homens')
print(f'{mulheres} são mulheres com menos de 20 anos')
