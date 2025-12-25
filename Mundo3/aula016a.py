"""
Curso Python #16 - Tuplas

Tupla é uma variável composta, pode armazenar mais de um dado.
Tuplas são imútaveis, ou seja, depois de atribuido um valor, não podemos alterar ou apagar.
Porém podemos apagar TODA a tupla.

Use tuplas quando:
- Os dados NÃO devem mudar
- Representam um registro fixo
- Precisam ser mais seguras
- Podem ser usadas como chave de dicionário

"""

# =========================================================
# 1️⃣ CRIAÇÃO DE TUPLAS
# =========================================================

# Tupla simples
tupla = (1, 2, 3)

# Tupla sem parênteses (packing)
tupla2 = 4, 5, 6

# Tupla com tipos mistos
tupla_mista = (1, 'Python', True, 3.14)

# Tupla com um único elemento (IMPORTANTE a vírgula)
tupla_um_elemento = (10,)

# Sem vírgula, NÃO é tupla
nao_e_tupla = (10)

print(type(tupla_um_elemento))
print(type(nao_e_tupla))


# =========================================================
# 2️⃣ ACESSO A ELEMENTOS
# =========================================================

numeros = (10, 20, 30, 40)

print(numeros[0])     # Primeiro elemento
print(numeros[-1])    # Último elemento


# =========================================================
# 3️⃣ FATIAMENTO (SLICING)
# =========================================================

print(numeros[1:3])   # Do índice 1 até antes do 3
print(numeros[:2])    # Do início até o índice 2
print(numeros[2:])    # Do índice 2 até o fim
print(numeros[::2])   # Pula de 2 em 2
print(numeros[::-1])  # Inverte a tupla


# =========================================================
# 4️⃣ IMUTABILIDADE
# =========================================================

# numeros[0] = 99
# ❌ Isso gera erro: TypeError
# Tuplas NÃO permitem alteração direta


# =========================================================
# 5️⃣ ITERAÇÃO COM FOR
# =========================================================

for i in range(0, len(numeros)):
    print(numeros[i])

for n in numeros:
    print(n)

# Com índice
for i, valor in enumerate(numeros):
    print(f'Índice {i} → {valor}')


# =========================================================
# 6️⃣ OPERAÇÕES COM TUPLAS
# =========================================================

a = (1, 2, 3)
b = (4, 5)

# Concatenação
c = a + b
print(c)

# Repetição
d = a * 3
print(d)


# =========================================================
# 7️⃣ FUNÇÕES NATIVAS
# =========================================================

print(len(numeros))   # Tamanho
print(max(numeros))   # Maior valor
print(min(numeros))   # Menor valor
print(sum(numeros))   # Soma (se forem números)


# =========================================================
# 8️⃣ CONTAGEM E BUSCA
# =========================================================

dados = (1, 2, 2, 3, 2, 4)

print(dados.count(2))     # Quantas vezes aparece
print(dados.index(3))     # Índice da primeira ocorrência


# =========================================================
# 9️⃣ DESEMPACOTAMENTO (UNPACKING)
# =========================================================

pessoa = ('Maylon', 21, 'Backend')

nome, idade, area = pessoa # Atribui Maylon, 21 e Backend respectivamente
print(nome)
print(idade)
print(area)

# Desempacotamento parcial
a, b, *resto = (1, 2, 3, 4, 5) # Atribui 1 para a, 2 para b e 3, 4 e 5 para resto
print(a, b, resto)


# =========================================================
# 🔟 TUPLAS DENTRO DE TUPLAS (MATRIZ SIMPLES)
# =========================================================

cadastro = (
    ('Ana', 20),
    ('João', 25),
    ('Maria', 22)
)

for nome, idade in cadastro:
    print(f'{nome} tem {idade} anos')


# =========================================================
# 1️⃣1️⃣ CONVERSÕES
# =========================================================

lista = list(numeros)   # Tupla → Lista
lista.append(50)
numeros_novos = tuple(lista)  # Lista → Tupla

print(numeros_novos)


# =========================================================
# 1️⃣2️⃣ TESTE DE PERTINÊNCIA
# =========================================================

print(20 in numeros) # Verifica se 20 está em numeros
print(99 not in numeros) # Verifica se 99 não está em números
