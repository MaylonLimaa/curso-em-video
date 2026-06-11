"""
Esses são ou métodos mágicos ou dunder(double under) methods. 
__init__: É o método construtor ou inicializador, utilizado para configurar o estado inicial dos objetos assim que são criados.
__doc__: Um atributo especial que armazena a documentação da classe (conhecida como docstring), permitindo que desenvolvedores consultem o "manual" de uso de uma classe.
__str__: Um método que permite personalizar a exibição do objeto. Ao sobrescrevê-lo, é possível definir uma representação amigável em formato de texto para quando o objeto for impresso, em vez de apenas exibir seu endereço de memória.
__dict__: Um atributo que exibe o estado interno do objeto no formato de um dicionário.
__getstate__: Um método que também permite visualizar o estado interno do objeto, com a vantagem de poder ser customizado pelo programador para formatar a exibição desses dados.
__class__: Um atributo que revela a qual classe um determinado objeto pertence.
"""

#Classe
class Gafanhoto:
    """
    O que compõe uma boa Docstring?
    Uma docstring de alta qualidade deve responder a três perguntas principais para quem está lendo seu código:
        1. O que a função/classe faz? 
        2. Quais argumentos ela recebe (e de que tipo)?
        3. O que ela retorna?
    """
    #Construtor
    def __init__(self, nome ='', idade = 0):
        """
        __init__: É o método construtor ou inicializador, utilizado para configurar o estado inicial dos objetos assim que são criados.
        """
        self.nome = nome
        self.idade = idade

    # Método de instancias
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        """
        __str__: Um método que permite personalizar a exibição do objeto. Ao sobrescrevê-lo, é possível definir uma representação amigável em formato de texto para quando o objeto for impresso, em vez de apenas exibir seu endereço de memória.
        """
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

    def __getstate__(self):
        """
        __getstate__: Um método que também permite visualizar o estado interno do objeto, com a vantagem de poder ser customizado pelo programador para formatar a exibição desses dados.
        """
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# Declaração de objetos
g1 = Gafanhoto('Maylon', 21)

print(g1)

print('-'*100)

print('__doc__: Um atributo especial que armazena a documentação da classe (conhecida como docstring), permitindo que desenvolvedores consultem o "manual" de uso de uma classe.')
print(Gafanhoto().__doc__)

print('-'*100)

print('__dict__: Um atributo que exibe o estado interno do objeto no formato de um dicionário.')
print(g1.__dict__)

print('-'*100)

print('__class__: Um atributo que revela a qual classe um determinado objeto pertence.')
print(g1.__class__)
