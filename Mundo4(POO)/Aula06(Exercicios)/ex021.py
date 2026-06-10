"""#### 🖊️ Desafio 21: Classe Caneta
* **Objetivo:** Controlar o estado e o funcionamento de um objeto simples.
* **Atributos:** `cor` (permitir estritamente apenas `azul`, `vermelha` ou `verde`) e `tampada` (booleano).
* **Regra/Método:** Métodos para tampar/destampar e um método para simular a escrita. A classe deve validar: se tentar escrever com a caneta tampada, ela deve retornar uma mensagem de erro ou impedir a ação.
"""

from rich import print

class Caneta:
    def __init__(self, cor):
        if cor not in ["azul", "vermelha", "verde"]:
            self.cor = "azul"
        else:
            self.cor = cor
        self.tampada = True

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, texto):
        if self.tampada:
            return "[bold red]Erro: Não é possível escrever com a caneta tampada.[/bold red]"

        # Mapeia a cor para a tag em inglês do Rich
        cores_rich = {"azul": "blue", "vermelha": "red", "verde": "green"}
        tag_cor = cores_rich[self.cor]

        return f"Escrevendo em {self.cor}: [{tag_cor}]{texto}[/{tag_cor}]"


# Execução direta
minha_caneta = Caneta("azul")

print(minha_caneta.escrever("Testando a caneta..."))  # Alerta de erro em vermelho negrito
minha_caneta.destampar()
print(minha_caneta.escrever("Agora vai!")) # O texto sai na cor vermelha do Rich
