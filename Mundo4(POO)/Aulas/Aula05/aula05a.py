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
        nome = '' e idade = 0 : Seleciona esses valores como padrão para estes parâmetros, caso não indique valor, o sistema define automaticamente como vazio('') e idade como 0.
        """
        self.nome = nome
        self.idade = idade

    # Método de instancias
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

# Declaração de objetos
g1 = Gafanhoto('Maylon', 21)
# Inicia-se o objeto já com um Nome e Idade.
print(g1.mensagem())
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto('Clara', 25)
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())
