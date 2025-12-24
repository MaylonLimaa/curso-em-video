"""
Desafio 83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta.
"""

expressao = str(input('Digite a expressão: '))
pilha = []

for caractere in expressao:
    if caractere == '(':
        # Toda vez que um parênteses abre, "empilhamos" ele na lista
        pilha.append('(')
    elif caractere == ')':
        # Se encontramos um fechamento, precisamos verificar se havia algo aberto
        if len(pilha) > 0:
            # Se a pilha não está vazia, "desempilhamos" (removemos o último '(')
            pilha.pop()
        else:
            # Se a pilha está vazia e tentamos fechar, a expressão já está errada
            pilha.append(')')
            break

# Ao final, se a pilha estiver totalmente vazia, significa que tudo que abriu, fechou.
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')