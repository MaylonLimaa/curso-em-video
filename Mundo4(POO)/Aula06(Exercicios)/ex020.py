"""
#### 🎮 Desafio 20: Classe Gamer
* **Objetivo:** Montar a ficha de perfil de um jogador.
* **Atributos:** `nome`, `nick` e uma lista (`list`) de jogos favoritos.
* **Regra/Método:** Um método que retorne a ficha completa do jogador, garantindo que a lista de jogos favoritos seja apresentada organizada em **ordem alfabética**.
"""

class Gamer:
    def __init__(self, nome, nick, jogos_favoritos):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = jogos_favoritos

    def obter_ficha(self):
        jogos_ordenados = sorted(self.jogos_favoritos)
        return (
            f"Nome: {self.nome}\n"
            f"Nick: {self.nick}\n"
            f"Jogos Favoritos: {', '.join(jogos_ordenados)}"
        )


# Execução direta
player = Gamer("Maylon", "MaylonLimaa", ["Resident Evil 4", "Resident Evil 4 Remake", "Resident Evil Code Veronica"])
print(player.obter_ficha())
