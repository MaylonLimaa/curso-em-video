"""
Desafio 76: Crie um programa que tenha uma tupla única com nomes de produtos 
e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, 
organizando os dados em forma tabular.
"""

produtos = (
    ('Água', 1.5),
    ('Livro', 5),
    ('Bicicleta', 1000)
)
print('|', '-'*50, '|')
print(f'| {' '*16}listagem de preços{' '*16} |')
print('|', '-'*50, '|')
for i, p in produtos:
    print(f'|{i:.<40} R$ {p:>7.2f} |')
print('|', '-'*50, '|')