"""#### 📺 Desafio 22: Classe Controle Remoto
* **Objetivo:** Modelar as interações de um dispositivo controlador de TV.
* **Atributos:** `ligada` (booleano), `volume_atual` e `canal_atual`.
* **Regra/Método:** * Ligar e desligar o aparelho.
    * Aumentar/Diminuir volume (com travas de limite mínimo de 0 e máximo de 100).
    * Mudar de canal (avançar/retroceder ou ir para um canal específico, validando se o canal é positivo).
    * *Regra de Ouro:* Bloquear qualquer alteração de volume ou canal se a TV estiver desligada.
"""

from rich import print

class ControleRemoto:
    def __init__(self):
        self.ligada = False
        self.volume_atual = 20  # Inicia em um volume padrão
        self.canal_atual = 1    # Inicia no canal 1

    def ligar_desligar(self):
        self.ligada = not self.ligada
        estado = "[green]LIGADA[/green]" if self.ligada else "[red]DESLIGADA[/red]"
        return f"A TV foi {estado}."

    def alterar_volume(self, quantidade):
        if not self.ligada:
            return "[bold red]Erro: Não é possível alterar o volume com a TV desligada.[/bold red]"

        novo_volume = self.volume_atual + quantidade

        # Travas de limite (0 a 100)
        if novo_volume > 100:
            self.volume_atual = 100
        elif novo_volume < 0:
            self.volume_atual = 0
        else:
            self.volume_atual = novo_volume

        return f"Volume atual: [blue]{self.volume_atual}[/blue]"

    def mudar_canal(self, canal):
        if not self.ligada:
            return "[bold red]Erro: Não é possível mudar de canal com a TV desligada.[/bold red]"

        if canal <= 0:
            return "[bold yellow]Aviso: O canal deve ser um número positivo.[/bold yellow]"

        self.canal_atual = canal
        return f"Canal atual: [magenta]{self.canal_atual}[/magenta]"


# Execução direta
controle = ControleRemoto()

# Tentando mexer com ela desligada
print(controle.alterar_volume(10))

# Ligando a TV
print(controle.ligar_desligar())

# Mexendo no volume e canal
print(controle.alterar_volume(15))   # Vai para 35
print(controle.alterar_volume(100))  # Trava no 100
print(controle.mudar_canal(5))       # Vai para o canal 5
print(controle.mudar_canal(-2))      # Bloqueia canal inválido

# Desligando a TV
print(controle.ligar_desligar())
