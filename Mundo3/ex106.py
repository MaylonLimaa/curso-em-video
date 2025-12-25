"""
Desafio 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar 
a palavra 'FIM', o programa se encerrará. Importante: use cores.
"""

def ajuda():
    while True:
        print('Para parar digite FIM')

        cmd = input('Quando comando deseja verificar o manual? ')
        if cmd.upper() == 'FIM':
            return
        help(cmd.lower())


ajuda()
