
"""
Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""

vlr = float(input('Qual o valor do produto? '))
print('1 - Á vista dinheiro/cheque | '
    '2 - À vista cartão | '
    '3 - Parcela em até 2x | ' 
    '4 -  Parcelado em mais de 3x')
opcao = int(input('Qual a forma de pagamento??'))
if opcao > 4 or opcao < 1:
    print('Opção inválida')
match opcao:
    case 1:
        vlrtotal = vlr * 0.9
        print(f' O valor com desconto de 10% é {vlrtotal} ')
    case 2:
        vlrtotal = vlr * 0.95
        print(f' O valor com desconto de 5% é {vlrtotal} ')
    case 3:
        print('Não há desconto para esta forma de pagamento')    
    case 4:
        vlrtotal = vlr * 1.2
        print(f' O valor com juros de 20% é {vlrtotal} ')
