"""Desafio 16: Classe Funcionário
Objetivo: Criar uma classe para cadastrar as informações básicas de um colaborador.
Atributos: `nome`, `setor` e `cargo`.
Regra/Método: Um método que retorne uma string de apresentação com os dados do funcionário (ex: *"Olá, meu nome é [Nome], trabalho no setor de [Setor] como [Cargo]"*)."""

# Área de Classes
class Funcionario:
    """Classe simples que representa um funcionário.
    """
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
 
    def __str__(self):
        return f'Olá, meu nome é {self.nome}, trabalho como {self.cargo} no setor {self.setor}'

# Programa principal
p1 = Funcionario('Pedro', 'Gerente de Projetos', 'TI')
p2 = Funcionario('Ana', 'Supervisora', 'Marketing')

print(p1)
print(p2)
