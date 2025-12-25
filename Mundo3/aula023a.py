"""
Curso Python #23 - Tratamento de Erros e Exceções

GUIA COMPLETO - TRY / EXCEPT EM PYTHON
Autor: Exemplo didático
Objetivo: Demonstrar, em UM ÚNICO ARQUIVO, todas as formas corretas
de uso do try / except em Python.
"""

# ==========================================================
# 1) TRY / EXCEPT BÁSICO
# ==========================================================

print("\n--- EXEMPLO 1: try/except básico ---")

try:
    n = int(input("Digite um número inteiro: "))
except:
    print("Erro! Você não digitou um número inteiro.")
else:
    print(f"Você digitou o número {n}")


# ==========================================================
# 2) TRATANDO ERROS ESPECÍFICOS (BOA PRÁTICA)
# ==========================================================

print("\n--- EXEMPLO 2: erros específicos ---")

try:
    n = int(input("Digite um número para dividir 10 por ele: "))
    resultado = 10 / n
except ValueError:
    print("Erro: isso não é um número.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
else:
    print(f"Resultado da divisão: {resultado}")


# ==========================================================
# 3) USANDO finally (SEMPRE EXECUTA)
# ==========================================================

print("\n--- EXEMPLO 3: finally ---")

try:
    arquivo = open("arquivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    print("Esse bloco SEMPRE executa.")


# ==========================================================
# 4) CAPTURANDO O ERRO EM UMA VARIÁVEL
# ==========================================================

print("\n--- EXEMPLO 4: capturando o erro ---")

try:
    x = int("abc")
except ValueError as erro:
    print("O erro ocorrido foi:")
    print(erro)


# ==========================================================
# 5) TRY / EXCEPT DENTRO DE FUNÇÃO (CASO REAL)
# ==========================================================

print("\n--- EXEMPLO 5: função protegida ---")

def leia_int(msg):
    while True:
        try:
            valor = int(input(msg))
        except ValueError:
            print("ERRO! Digite um número inteiro válido.")
        else:
            return valor

numero = leia_int("Digite um número inteiro seguro: ")
print(f"Número recebido com sucesso: {numero}")


# ==========================================================
# 6) TRY / EXCEPT + raise (CRIANDO ERRO)
# ==========================================================

print("\n--- EXEMPLO 6: raise ---")

def sacar(valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser positivo.")
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

try:
    sacar(-10)
except ValueError as erro:
    print(f"Erro no saque: {erro}")


# ==========================================================
# 7) EXEMPLO DO QUE NÃO FAZER
# ==========================================================

print("\n--- EXEMPLO 7: o que NÃO fazer ---")

try:
    x = 10 / 0
except:
    pass  # ISSO ESCONDE ERROS — EVITE!