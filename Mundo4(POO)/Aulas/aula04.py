"""
Classes: A declaração de uma classe é feita usando a palavra "class" antes do nome da classe. 
class Classe.
Objeto: O instanciamento de um objeto é feito declarando uma variável atribuida a uma classe. 
Objeto = Classe().

Método construtor: 
Este método é chamado no momento em que você instancia um objeto, ele valida os atributos do Objeto. 
Ele é um "método mágico". A escrita dele é desta forma: __init__(self).
"""

class Gafanhoto:
    """
    Classe para aprendizado de criação de classes, métodos, atributos e instacimento de objetos
    """
    def __init__(self):
        """Método construtor"""
        self.nome = ""
        self.idade = 0

    # Método de instancias
    def aniversario(self):
        """Sempre que é chamado, adiciona mais 1 a idade."""
        self.idade += 1

    def mensagem(self):
        """Retorna uma apresentação"""
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

# Declaração de objetos
g1 = Gafanhoto()
g1.nome = 'Maylon'
g1.idade = 21
print(g1.mensagem())
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Clara'
g2.idade = 25
print(g2.mensagem())
