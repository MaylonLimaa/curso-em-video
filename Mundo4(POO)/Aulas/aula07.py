"""
Herança em Python explicada como nunca fizeram - Curso Python POO: Aula 7

Os quatro pilares da POO são: Abstração, Encapsulamento, Polimorfismo e Herança.
Neste arquivo, vamos abordar a herança.

Herança: é um relacionamento entre elementos gerais (ancestrais) e tipos mais específicos (descendentes), que herdam atributos e métodos dos níveis superiores.

Principais vantagens:
- Reutilização de código;
- Organização hierárquica;
- Facilidade de manutenção;
- Extensibilidade;
- Suporte ao polimorfismo.

A herança por generalização representa um relacionamento do tipo "É UM".
"""

class Pessoa:
    """Classe Pessoa. Classe genérica que representa uma pessoa.
    Está classe foi criada para exemplificar na prática como funciona herança.
    Atributos: Nome e Idade.
    Método: fazerAniversario()
    Trata-se de uma superclasse ou classe mãe.
    """
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    """Classe especializada, descendente, subclasse ou classe filho de Pessoa.
    Para herdar, basta, ao declarar a classe, abrir e fechar paretênses e passar a classe que vai ser herdade como parâmetro.
    """
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) # Método para chamar o construtor da classe mãe
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'{self.nome} fez a matrícula!')


class Professor(Pessoa):
    """Classe especializada, descendente, subclasse ou classe filho de Pessoa.
    Para herdar, basta, ao declarar a classe, abrir e fechar paretênses e passar a classe que vai ser herdade como parâmetro.
    """
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    def dar_aula(self):
        print(f'{self.nome} está dando aula!')


class Funcionario(Pessoa):
    """Classe especializada, descendente, subclasse ou classe filho de Pessoa.
    Para herdar, basta, ao declarar a classe, abrir e fechar paretênses e passar a classe que vai ser herdade como parâmetro.
    """
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    def bater_ponto(self):
        print(f'{self.nome} registrou o ponto!')

a1 = Aluno('Maylon', 22, 'Eng de Software', 'T001ES')
p1 = Professor('Claúdio', 47, 'Programação Web', 'Mestrado')
f1 = Funcionario('Ana', 30, 'Diretora', 'ADM')

a1.fazer_aniversario()
print(a1.idade)
a1.fazer_matricula()
