"""
========================================
ANOTAÇÕES SOBRE FUNÇÕES EM PYTHON
========================================

Este arquivo serve como bloco de notas.
Leia, execute, modifique e teste.

FOCO:
- O que é função
- Quando usar
- Como usar corretamente
- Boas práticas
"""

# ---------------------------------------
# 1) O que é uma função
# ---------------------------------------
# Uma função é um bloco de código que:
# - recebe dados (parâmetros)
# - processa esses dados
# - devolve um resultado (return)

def soma(a, b):
    return a + b


resultado = soma(2, 3)
print(resultado)  # 5


# ---------------------------------------
# 2) Função SEM return
# ---------------------------------------
# Se não houver return, a função devolve None

#def mostrar_soma(a, b):
#    print(a + b)

# x = mostrar_soma(2, 3)
# print(x)  # None


# ---------------------------------------
# 3) Regra importante
# ---------------------------------------
# Funções devem CALCULAR.
# Quem chama decide se imprime, salva ou usa o valor.


# ---------------------------------------
# 4) Função pura (modelo ideal)
# ---------------------------------------
# - Não usa input()
# - Não usa print()
# - Não depende de variável externa
# - Sempre retorna algo

def media(n1, n2):
    return (n1 + n2) / 2


m = media(7, 5)
print(m)


# ---------------------------------------
# 5) Função com decisão lógica
# ---------------------------------------

def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


print(situacao_aluno(7))
print(situacao_aluno(4))


# ---------------------------------------
# 6) Função trabalhando com listas
# ---------------------------------------

def maior_valor(lista):
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior


numeros = [3, 7, 1, 9, 4]
print(maior_valor(numeros))


# ---------------------------------------
# 7) Função trabalhando com dicionários
# ---------------------------------------

def ordenar_por_resultado(jogadores):
    return sorted(
        jogadores.values(),
        key=lambda jogador: jogador['resultado'],
        reverse=True
    )


# Exemplo de uso:
jogadores = {
    'Pedro': {'nome': 'Pedro', 'resultado': 4},
    'Ana': {'nome': 'Ana', 'resultado': 6},
    'Davi': {'nome': 'Davi', 'resultado': 4}
}

ranking = ordenar_por_resultado(jogadores)

for jogador in ranking:
    print(jogador['nome'], '->', jogador['resultado'])


# ---------------------------------------
# 8) Função chamando outra função
# ---------------------------------------

def calcular_media(notas):
    return sum(notas) / len(notas)


def avaliar_aluno(notas):
    media = calcular_media(notas)
    return situacao_aluno(media)


print(avaliar_aluno([7, 8, 6]))
print(avaliar_aluno([4, 5, 3]))


# ---------------------------------------
# 9) Função NÃO deve fazer tudo
# ---------------------------------------
# ERRADO:
# - lê input
# - calcula
# - imprime
# - decide

# CERTO:
# - uma função para cada responsabilidade

# ---------------------------------------
# 10) Função como contrato
# ---------------------------------------
# Quem usa a função NÃO precisa saber como ela funciona,
# apenas:
# - o que entra
# - o que sai
