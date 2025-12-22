"""
Curso Python #15 - Interrompendo repetições while

Optei por considerar as aulas 14 e 15 como continuações uma das outras
"""
print("=== Exemplo 4: While com continue ===")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # pula o print quando i é 3
    print(i)
print("Fim do loop com continue\n")

# ===============================
print("=== Exemplo 5: While True + Break (Loop infinito controlado) ===")
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    print(f"Você digitou: {n}")
print("Fim do loop while True com break\n")

# ===============================
print("=== Exemplo 6: Menu com while True e break ===")
while True:
    print("1 - Opção A")
    print("2 - Opção B")
    print("0 - Sair")
    escolha = input("Escolha: ")
    if escolha == "0":
        break
    else:
        print(f"Você escolheu: {escolha}")
print("Fim do menu\n")

# ===============================
print("=== Exemplo 7: Validação de entrada com while True ===")
while True:
    senha = input("Digite sua senha (mínimo 6 caracteres): ")
    if len(senha) >= 6:
        print("Senha aceita!")
        break
    else:
        print("Senha muito curta, tente novamente.")
print("Fim do loop de validação\n")
