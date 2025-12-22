"""
Desafio 58: Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer.
"""

from random import randint

NUM = randint(0, 10)
numusuario = int(input('Digite um número entre 0 a 10: '))
tentativas = 1

while numusuario != NUM:
    tentativas += 1
    print('Infelizmente você errou! Tente novamente')
    numusuario = int(input('Digite um número entre 0 a 10: '))

print(f'Parabéns você acertou! O número realmente era {NUM}')
print(f'Você tentou {tentativas} vezes')
