"""
Este arquivo complementa o conteúdo do aula016a.py
Aqui NÃO há criação, indexação, slicing básico, for simples, etc.

O foco aqui é:
- Como tuplas são usadas DE VERDADE
- Por que elas existem desse jeito
- Como a linguagem Python se apoia nelas

Tuplas não representam ação.
Tuplas representam ESTADO.

Métodos normalmente implicam mudança.
Como tuplas não mudam, não faz sentido terem muitos métodos.

Por isso:
- Poucos métodos próprios
- Uso intenso de funções externas
- Integração profunda com o core do Python
"""

# =========================================================
# 1️⃣ sorted() — operar sem modificar a tupla
# =========================================================

# Tuplas são imutáveis, logo NÃO possuem método .sort()
# Porém, podemos ORDENAR seus dados usando a função sorted()

t = (5, 1, 4, 2)

ordenado = sorted(t)
print(ordenado)        # Retorna LISTA
print(type(ordenado)) # <class 'list'>

# Se quisermos manter como tupla:
ordenado_tupla = tuple(sorted(t))
print(ordenado_tupla)


# =========================================================
# 2️⃣ Comparação entre tuplas (ordem lexicográfica)
# =========================================================

# Python compara elemento por elemento, da esquerda para a direita
print((1, 2, 3) < (1, 2, 4))   # True
print((2, 0) > (1, 100))       # True

# Uso real:
# - ordenações
# - algoritmos
# - estruturas internas do Python


# =========================================================
# 3️⃣ Tuplas como CHAVE de dicionário
# =========================================================

# Apenas tipos IMUTÁVEIS podem ser chaves
# Tuplas são imutáveis → podem ser chaves

coordenadas = {
    (10, 20): 'Ponto A',
    (30, 40): 'Ponto B'
}

print(coordenadas[(10, 20)])

# Isso NÃO funcionaria com listas:
# coordenadas[[10, 20]] = 'Erro'


# =========================================================
# 4️⃣ hash() — por que tuplas funcionam como chave
# =========================================================

t = (1, 2, 3)
print(hash(t))

# hash() gera um identificador fixo
# Como a tupla não muda, o hash nunca muda
# Isso é a base de dicionários, sets, caches, etc.


# =========================================================
# 5️⃣ zip() — criação estruturada de tuplas
# =========================================================

nomes = ('Ana', 'João', 'Maria')
idades = (20, 25, 22)

dados = tuple(zip(nomes, idades))
print(dados)

# Resultado:
# (('Ana', 20), ('João', 25), ('Maria', 22))

# Muito usado para:
# - importar dados
# - sincronizar informações
# - criar registros imutáveis


# =========================================================
# 6️⃣ Desempacotamento com descarte (_)
# =========================================================

pessoa = ('Maylon', 21, 'Backend')

nome, _, area = pessoa
print(nome)
print(area)

# _ significa:
# "esse valor existe, mas não me importa"


# =========================================================
# 7️⃣ Retorno múltiplo de funções (contrato)
# =========================================================

def calcular(a, b):
    # Retorna uma tupla implicitamente
    return a + b, a * b

soma, produto = calcular(2, 3)
print(soma, produto)

# Aqui a tupla NÃO é coleção
# Ela é um CONTRATO de retorno


# =========================================================
# 8️⃣ Tuplas como ENUM simples
# =========================================================

# Quando você quer constantes organizadas e seguras
CORES = ('VERMELHO', 'VERDE', 'AZUL')

print(CORES[0])

# Não muda
# Não quebra
# Não precisa de classe
# Extremamente comum


# =========================================================
# 9️⃣ Tupla + sorted + key (padrão profissional)
# =========================================================

pessoas = (
    ('Ana', 20),
    ('João', 25),
    ('Maria', 22)
)

# Ordenar por idade
ordenado_por_idade = sorted(pessoas, key=lambda p: p[1])
print(ordenado_por_idade)

# sorted → lista
# lambda → critério
# tupla → estrutura fixa
