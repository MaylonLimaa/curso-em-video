
"""
Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) 
e mostre seu status, conforme a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

alt = float(input('Qual sua altura em Metros? '))
peso = float(input('Qual seu peso em KG? '))
imc = peso / (alt ** 2)

if imc > 40:
    print('Obesidade mórbida')
elif imc > 30:
    print('Obesidade')
elif imc > 25:
    print('Sobrepeso')
elif imc > 18.5:
    print('Peso Ideal')
else:
    print('Abaixo do peso')
