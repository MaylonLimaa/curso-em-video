"""Abstração um dos Pilares Centrais da Programação Orientada a Objetos- Curso Python POO: Aula 8
Abstração: A prática de ignorar o irrelevante e se forçar estritamente no essencial.

Principais vantagens:
- Maior Legibilidade.
- Padronização.
- Simplificação.
- Segurança.

Existe a abstração de dados, que acontece quando ignoramos informações desnecessárias para o escopo do projeto.
Por exemplo, uma pessoa pode ter muitas informações. Peso, nome, idade, cpf, etc.
Caso fossemos fazer um sistema para uma escola, o peso pode não ser um atributo necessário de armazenar, sendo assim, não precisamos usar esta informação.

Existe a abstração de processos, é quando não precisamos saber como um método faz seu trabalho, apenas sabe que ele existe pela interface.

Classe abstrata é uma classe usada apenas como base para outras classes(subclasses). A classe abstrata nunca vai ser instanciada. Uma classe abstrata pode ter métodos que deverão ser obrigatoriamente implementados nas subcasse. Uma classe abstrata pode ter métodos concretos, caso eles sejam implementados da mesma forma em todas as subclasses.
Método concreto é um método que as subclasses herdam e não fazem alterações, todos usam da mesma forma.
Método abstrato é um metodo que as subclasses herdam mas podem fazer alterações. Para reprensentar métodos abstratos usamos "{abstract}". Na super classe um método abstrato não possui código, os códigos são feitos nas subclasses. 
"""

from abc import ABC, abstractmethod #Abstract Base Classes

class Pessoa(ABC):
    """
    Quando a classe Pessoa herdou a classe ABC ela se tornou uma classe abstrata.
    """
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) # Método para chamar o construtor da classe mãe
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'{self.nome} fez a matrícula!')
    
    def estudar(self):
        print('Estudando a matéria')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    def dar_aula(self):
        print(f'{self.nome} está dando aula!')

    def estudar(self):
        print('Estudando o conteúdo para a aula!')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    def bater_ponto(self):
        print(f'{self.nome} registrou o ponto!')

    def estudar(self):
        print(f'Estudando sobre a escola!')

a1 = Aluno('Maylon', 22, 'Eng de Software', 'T001ES')
p1 = Professor('Claúdio', 47, 'Programação Web', 'Mestrado')
f1 = Funcionario('Ana', 30, 'Diretora', 'ADM')

a1.fazer_aniversario() # Mostra uso do método herdado
print(a1.idade) # Print do atributo
a1.fazer_matricula()

