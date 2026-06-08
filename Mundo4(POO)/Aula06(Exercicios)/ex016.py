"""Desafio 16: Classe Funcionário
Objetivo: Criar uma classe para cadastrar as informações básicas de um colaborador.
Atributos: `nome`, `setor` e `cargo`.
Regra/Método: Um método que retorne uma string de apresentação com os dados do funcionário (ex: *"Olá, meu nome é [Nome], trabalho no setor de [Setor] como [Cargo]"*).

Atributos de classes são compartilhados com todos os objetos, ou seja, todos os objetos tem o mesmo atributo com o mesmo valor atribuído. E, caso altere o valor destes atributos, vai alterar para TODOS os objetos. 
Métodos de instância são métodos que cada objeto possui individualmente, ou seja, caso alterado o valor para um objeto não altera o valor para outro.
"""

# Área de Classes
class Funcionario:
    """Classe simples que representa um funcionário.
    """
    #Métodos de Classes
    empresa = 'Teste LTDA'
    def __init__(self, nome, setor, cargo):
        #Métodos de Instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
 
    def __str__(self):
        return f'Olá, meu nome é {self.nome}, trabalho como {self.cargo} no setor {self.setor} da empresa {Funcionario.empresa}'

# Programa principal
p1 = Funcionario('Pedro', 'Gerente de Projetos', 'TI')
p2 = Funcionario('Ana', 'Supervisora', 'Marketing')

print(p1)
print(p2)
