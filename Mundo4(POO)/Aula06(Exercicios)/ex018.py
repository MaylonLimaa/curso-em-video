"""Desafio 18: Classe Churrasco
* **Objetivo:** Criar uma calculadora para gerenciar os custos e insumos de um evento.
* **Atributos:** Preço fixo por quilo da carne (definido na instância).
* **Regra/Método:** Receber o número de pessoas e calcular:
    * A quantidade total de carne necessária (baseada em um consumo de 400g por pessoa).
    * O custo total da carne.
    * O valor rateado por pessoa.
    * *Nota: O método deve retornar esses dados estruturados (ou em formato de texto descritivo) para que o programa principal decida como exibir.*
"""

class Churrasco:
    def __init__(self, preco):
        self.preco = preco
    
    def calcChurras(self, pessoas):
        totalcarne = (pessoas * 400) / 1000
        precocarne = totalcarne * self.preco
        rateio = precocarne / pessoas

        return f'Para {pessoas} pessoas o total de carne é {totalcarne}KG no preço total de {precocarne:.2f} e rateado fica R$ {rateio:.2f} para cada'

c1 = Churrasco(15.5)
print(c1.calcChurras(15))
