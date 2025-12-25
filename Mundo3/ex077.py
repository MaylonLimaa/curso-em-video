"""
Desafio 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('Agua', 'Pedra', 'Pedro', 'Claro', 'Escuro')

for palavra in palavras:
    print(f'A palavra {palavra} possui as vogais: ')
    for i, p in enumerate(palavra.lower()):
        if p in 'aeiou':
            print(p, end=' ')
    print()
