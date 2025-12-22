
"""
Desafio 59: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

opcao = 0
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))


while opcao != 5:
    print("""
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa
          """)
    opcao = int(input('Digite a opção: '))
    match opcao:
        case 1:
            s = n1 + n2
            print(f'{n1} + {n2} = {s}')
        case 2:
            s = n1 * n2
            print(f'{n1} x {n2} = {s}')
        case 3:
            if n1 > n2:
                print(f'{n1} é maior que {n2}')
            elif n2 > n1:
                print(f'{n2} é maior que {n1}')
            else:
                print('Os números são iguais')
        case 4:
            n1 = float(input('Digite o primeiro valor: '))
            n2 = float(input('Digite o segundo valor: '))
