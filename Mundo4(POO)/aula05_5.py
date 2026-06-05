"""
Anotações da biblioteca Rich

Instalação:
pip install rich
Documentação: rich.readthedocs.io
"""

# Importa o print da Rich.
# Ele substitui o print tradicional e permite usar cores,
# estilos e emojis.
from rich import print

# Permite criar painéis (caixas decoradas).
from rich.panel import Panel

# Permite criar tabelas formatadas.
from rich.table import Table

# Ferramenta para inspecionar objetos.
from rich import inspect

# Melhora a exibição de erros (tracebacks).
from rich.traceback import install


# ------------------------------------------------------------------
# TRACEBACK MELHORADO
# ------------------------------------------------------------------

# Ativa a exibição avançada de erros.
# Deve ser chamado logo no início do programa.
install()


# ------------------------------------------------------------------
# PRINT COLORIDO
# ------------------------------------------------------------------

print("\n[bold cyan]=== PRINT COLORIDO ===[/bold cyan]\n")

# Texto azul em negrito.
print("[bold blue]Olá, mundo![/bold blue]")

# Texto vermelho.
print("[red]Mensagem de erro.[/red]")

# Texto verde.
print("[green]Operação realizada com sucesso.[/green]")

# Combinação de estilos.
print("[bold yellow]Atenção![/bold yellow]")


# ------------------------------------------------------------------
# EMOJIS
# ------------------------------------------------------------------

print("\n[bold cyan]=== EMOJIS ===[/bold cyan]\n")

# A Rich converte códigos de emoji automaticamente.
print(":rocket: Projeto iniciado!")
print(":snake: Python")
print(":thumbs_up: Tudo funcionando!")
print(":warning: Atenção")


# ------------------------------------------------------------------
# PAINÉIS
# ------------------------------------------------------------------

print("\n[bold cyan]=== PANEL ===[/bold cyan]\n")

# Um painel é uma caixa visual usada para destacar informações.
painel = Panel(
    "Bem-vindo ao sistema!",
    title="Mensagem",
    subtitle="Rich",
)

print(painel)


# ------------------------------------------------------------------
# TABELAS
# ------------------------------------------------------------------

print("\n[bold cyan]=== TABLE ===[/bold cyan]\n")

# Cria uma tabela.
tabela = Table(title="Produtos")

# Adiciona colunas.
tabela.add_column("Produto", style="cyan")
tabela.add_column("Preço", style="green")

# Adiciona linhas.
tabela.add_row("Mouse", "R$ 50")
tabela.add_row("Teclado", "R$ 120")
tabela.add_row("Monitor", "R$ 800")

# Exibe a tabela.
print(tabela)


# ------------------------------------------------------------------
# INSPECT
# ------------------------------------------------------------------

print("\n[bold cyan]=== INSPECT ===[/bold cyan]\n")

# Classe simples para demonstração.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Meu nome é {self.nome}"


# Cria um objeto.
pessoa = Pessoa("Maylon", 22)

# Mostra informações do objeto:
# atributos, métodos e tipos.
inspect(pessoa)


# ------------------------------------------------------------------
# TRACEBACK (ERROS)
# ------------------------------------------------------------------

print("\n[bold cyan]=== TRACEBACK ===[/bold cyan]\n")

print(
    "Descomente a linha abaixo para ver "
    "o traceback avançado da Rich."
)

# Erro proposital.
# 1 / 0


# ------------------------------------------------------------------
# RESUMO
# ------------------------------------------------------------------

print("\n[bold green]Resumo:[/bold green]")

print(
    """
1. print()      -> texto colorido e emojis
2. Panel        -> caixas visuais
3. Table        -> tabelas formatadas
4. inspect()    -> inspeção de objetos
5. install()    -> erros mais fáceis de entender
"""
)
