"""
Desafio 49: Refaça o DESAFIO 9, mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um laço for.
"""
n = int(input('Digite um número: '))

print(f'{"="*15} Tabuada {"="*15}')
# Print de formatação que exibe tabuada centralizado com 15 simbolos = para cada lado
for i in range (1, 11):
    # Loop de repetição de 1 até 10
    print(f'{" "*10} {n} x {i} = {n*i}')
    # Exibe o resultado formatado em cada um dos loops