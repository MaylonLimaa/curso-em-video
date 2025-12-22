"""
Curso Python #014 - Estrutura de repetição while

Optei por considerar as aulas 14 e 15 como continuações uma das outras
"""

print("=== Exemplo 1: While simples (Contador) ===")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
print("Fim do contador\n")

# ===============================
print("=== Exemplo 2: While com múltiplas condições ===")
x, y = 3, 5
while x > 0 and y > 0:
    print(f"x={x}, y={y}")
    x -= 1
    y -= 2
print("Fim do loop múltiplas condições\n")

# ===============================
print("=== Exemplo 3: While com else ===")
i = 1
while i <= 3:
    print(i)
    i += 1

print("Loop terminou naturalmente\n")

# ===============================
