"""
Curso Python #19 - Dicionários
"""

# =========================
# 1️⃣ CRIAÇÃO DE DICIONÁRIO
# =========================

# Dicionário representa dados nomeados (chave → valor)
# Usamos quando a POSIÇÃO não importa, mas o SIGNIFICADO sim
pessoa = {
    "nome": "Maylon",
    "idade": 20,
    "ativo": True
}

# Chaves costumam ser strings (boas para legibilidade)
# Valores podem ser qualquer tipo


# =========================
# 2️⃣ ACESSO A DADOS
# =========================

# Acesso direto por chave
nome = pessoa["nome"]          # rápido e explícito
idade = pessoa["idade"]

# ⚠️ Se a chave não existir, isso gera erro
# pessoa["cpf"]  -> KeyError


# =========================
# 3️⃣ ACESSO SEGURO (get)
# =========================

# get evita erro se a chave não existir
cpf = pessoa.get("cpf")        # retorna None
cpf2 = pessoa.get("cpf", "não informado")

# Usamos get quando:
# - a chave pode não existir
# - queremos um valor padrão


# =========================
# 4️⃣ VERIFICAÇÃO DE CHAVES
# =========================

# "in" em dicionário verifica CHAVES, não valores
if "nome" in pessoa:
    pass  # sabemos que a chave existe

if "Maylon" in pessoa:
    pass  # isso é False (valores não contam)


# =========================
# 5️⃣ MODIFICAÇÃO DE VALORES
# =========================

# Dicionários são MUTÁVEIS
pessoa["idade"] = 21           # altera valor existente
pessoa["cidade"] = "SP"        # cria nova chave


# =========================
# 6️⃣ REMOÇÃO DE DADOS
# =========================

# Remove uma chave específica
del pessoa["ativo"]

# Remove e retorna o valor
idade_removida = pessoa.pop("idade")

# Remove o último item inserido (Python 3.7+)
ultimo = pessoa.popitem()


# =========================
# 7️⃣ ITERAÇÃO (percorrer)
# =========================

# Percorrendo apenas as chaves
for chave in pessoa:
    pass

# Percorrendo valores
for valor in pessoa.values():
    pass

# Percorrendo chave e valor (o mais comum)
for chave, valor in pessoa.items():
    pass


# =========================
# 8️⃣ TAMANHO DO DICIONÁRIO
# =========================

quantidade = len(pessoa)  # número de pares chave → valor


# =========================
# 9️⃣ CÓPIA DE DICIONÁRIO
# =========================

# Cópia rasa (shallow copy)
pessoa_copia = pessoa.copy()

# Alterar a cópia NÃO altera o original (para valores simples)
pessoa_copia["nome"] = "Outro"


# =========================
# 🔟 LIMPAR DICIONÁRIO
# =========================

pessoa.clear()  # remove tudo, mas mantém o objeto


# =========================
# 1️⃣1️⃣ DICIONÁRIOS ANINHADOS
# =========================

# Muito comum em sistemas reais
usuario = {
    "id": 1,
    "dados": {
        "nome": "Maylon",
        "email": "teste@email.com"
    }
}

# Acesso encadeado
email = usuario["dados"]["email"]


# =========================
# 1️⃣2️⃣ LISTA DE DICIONÁRIOS
# =========================

# Estrutura clássica para "registros"
alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "João", "nota": 6},
    {"nome": "Carlos", "nota": 9}
]

# Percorrendo registros
for aluno in alunos:
    if aluno["nota"] >= 7:
        pass


# =========================
# 1️⃣3️⃣ COMPARAÇÃO
# =========================

# == compara CONTEÚDO
a = {"x": 1, "y": 2}
b = {"y": 2, "x": 1}

print(a == b  )   # True (ordem não importa)

# is compara IDENTIDADE
print(a is b)     # False (objetos diferentes)
