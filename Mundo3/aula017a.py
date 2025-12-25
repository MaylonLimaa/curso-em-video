"""
Curso Python #17 - Listas (Parte 1) e (Parte 2)
Neste arquivo temos um tutorial extenso de como usar listas em python
"""

# --------------------------------------------
# 1. CRIAÇÃO DE LISTAS
# --------------------------------------------

# Lista comum: usada quando você precisa de uma coleção MUTÁVEL
lista = [1, 2, 3]

# Lista vazia: muito usada para construir dados ao longo do programa
lista_vazia = []

# Lista com tipos diferentes: Python permite, mas nem sempre é boa ideia
lista_mista = [1, "texto", True, 3.14]

# Lista aninhada: lista dentro de lista (estrutura hierárquica)
lista_aninhada = [[1, 2], [3, 4]]


# --------------------------------------------
# 2. ACESSO A ELEMENTOS
# --------------------------------------------

# Acesso por índice (listas são ORDENADAS)
primeiro = lista[0]      # pega o primeiro elemento
ultimo = lista[-1]       # pega o último elemento

# Fatiamento (slice): cria uma NOVA lista
sublista = lista[1:3]    # do índice 1 até o 2

# Cópia rasa da lista (novo objeto, mesmos elementos)
copia = lista[:]


# --------------------------------------------
# 3. ITERAÇÃO
# --------------------------------------------

# Iterar é percorrer elemento por elemento
# Usado quando você quer PROCESSAR dados
for item in lista:
    pass  # aqui você faria algo com cada item

# enumerate dá índice + valor
# Útil quando você precisa saber a posição
for indice, valor in enumerate(lista):
    pass


# --------------------------------------------
# 4. OPERADORES COM LISTAS
# --------------------------------------------

# in → verifica PRESENÇA
# Usado para validações
print(3 in lista)        # True

# not in → ausência
print(10 not in lista )  # True

# == → compara VALOR (conteúdo e ordem)
print([1, 2, 3] == [1, 2, 3])  # True

# is → compara IDENTIDADE (memória)
# Quase nunca usado com listas
print(lista is copia )   # False (objetos diferentes)

# + → concatena listas (gera nova lista)
nova_lista = lista + [4, 5]

# * → repete elementos
# Útil para inicialização
zeros = [0] * 5


# --------------------------------------------
# 5. MODIFICAÇÃO (LISTAS SÃO MUTÁVEIS)
# --------------------------------------------

# append → adiciona no final
# Usado quando a ordem importa
lista.append(4)

# insert → adiciona em posição específica
lista.insert(0, 0)

# extend → adiciona vários elementos
lista.extend([5, 6])

# Alteração direta por índice
lista[0] = 99

# Alteração por fatia
lista[1:3] = [20, 30]


# --------------------------------------------
# 6. REMOÇÃO DE ELEMENTOS
# --------------------------------------------

# remove → remove pelo VALOR (primeira ocorrência)
lista.remove(99)

# pop → remove e RETORNA
# Muito usado em pilhas
ultimo = lista.pop()

# pop com índice
primeiro = lista.pop(0)

# clear → limpa tudo
lista.clear()


# --------------------------------------------
# 7. BUSCAS
# --------------------------------------------

dados = [1, 2, 3, 2, 4]

# index → retorna o índice da primeira ocorrência
dados.index(2)

# count → conta quantas vezes aparece
dados.count(2)

# Busca manual (quando a condição é complexa)
for x in dados:
    if x == 3:
        break


# --------------------------------------------
# 8. ORDENAÇÃO
# --------------------------------------------

nums = [5, 3, 1, 4, 2]

# sort → ordena A PRÓPRIA lista
# Use quando você NÃO precisa da ordem original
nums.sort()

# reverse → ordem inversa
nums.sort(reverse=True)

# sorted → cria nova lista ordenada
# Use quando quer preservar a original
ordenada = sorted(nums)


# --------------------------------------------
# 9. FUNÇÕES QUE FUNCIONAM COM LISTAS
# --------------------------------------------

# len → tamanho
len(nums)

# min / max → menor e maior valor
min(nums)
max(nums)

# sum → soma
sum(nums)


# --------------------------------------------
# 10. COMPREENSÃO DE LISTAS
# --------------------------------------------

# Forma moderna e legível de criar listas
# Use quando a transformação é simples
quadrados = [x**2 for x in range(5)]

# Com condição
pares = [x for x in nums if x % 2 == 0]


# --------------------------------------------
# 11. MAP E FILTER (estilo funcional)
# --------------------------------------------

# map → transforma valores
dobro = list(map(lambda x: x * 2, nums))

# filter → filtra valores
so_pares = list(filter(lambda x: x % 2 == 0, nums))

# Hoje, compreensões são preferidas por legibilidade


# --------------------------------------------
# 12. DESEMPACOTAMENTO
# --------------------------------------------

# Atribuição múltipla
a, b, c = [1, 2, 3]

# *resto pega o restante
x, *resto = [1, 2, 3, 4]


# --------------------------------------------
# 13. LISTA COMO PILHA (STACK)
# --------------------------------------------

# LIFO: último a entrar, primeiro a sair
pilha = []
pilha.append(1)
pilha.append(2)
topo = pilha.pop()


# --------------------------------------------
# 14. LISTA COMO FILA (QUEUE SIMPLES)
# --------------------------------------------

# FIFO: primeiro a entrar, primeiro a sair
fila = []
fila.append(1)
fila.append(2)
primeiro = fila.pop(0)  # funciona, mas é lento


# --------------------------------------------
# 15. CÓPIA RASA VS PROFUNDA
# --------------------------------------------

import copy

original = [[1, 2], [3, 4]]

# Cópia rasa: compartilha objetos internos
rasa = original[:]

# Cópia profunda: tudo é copiado
profunda = copy.deepcopy(original)


# --------------------------------------------
# 16. LISTA COMO ESTADO
# --------------------------------------------

estado = []

# Lista vazia é False em contexto booleano
if not estado:
    estado.append("iniciado")


# --------------------------------------------
# 17. CONVERSÕES
# --------------------------------------------

# Lista para tupla (imutável)
tupla = tuple(nums)

# Lista para conjunto (remove duplicados)
conjunto = set(nums)

# String para lista
lista_chars = list("python")

# Lista para string (join exige strings)
texto = ",".join(["a", "b", "c"])


# --------------------------------------------
# 18. COMPARAÇÃO ENTRE LISTAS
# --------------------------------------------

# Comparação é lexicográfica (como palavras)
print([1, 2, 3] < [1, 2, 4])  # True


# --------------------------------------------
# 19. DELEÇÃO COM DEL
# --------------------------------------------

del nums[0]     # remove elemento
del nums[:2]    # remove fatia
