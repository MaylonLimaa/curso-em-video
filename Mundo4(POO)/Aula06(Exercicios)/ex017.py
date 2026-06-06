"""#### 🏷️ Desafio 17: Classe Produto
Objetivo: Gerenciar as informações de precificação de itens.
Atributos:`nome` e `preco`.
Regra/Método: Um método que monte e retorne uma string formatada simulando uma etiqueta de preço (ex: "[Produto] - R$ [Preço]" com duas casas decimais).
"""

# Área de Importações
from rich.table import Table
from rich import print

# Classes
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        if isinstance(self.preco, int) or isinstance(self.preco, float):
            temp = f'R$ {self.preco:.2F}'
        tabela = Table(title = 'Etiqueta')
        tabela.add_column('Nome')
        tabela.add_column('Preço')
        tabela.add_row(self.nome, temp)
        return tabela

# Seção principal
p1 = Produto('Água', 2)
p2 = Produto('Garrafa', 5.5)
p3 = Produto('Moto', 8999.90)
print(p1.etiqueta())
print(p2.etiqueta())
print(p3.etiqueta())
