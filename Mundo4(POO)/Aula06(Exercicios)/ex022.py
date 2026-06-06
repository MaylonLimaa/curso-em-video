"""#### 📺 Desafio 22: Classe Controle Remoto
* **Objetivo:** Modelar as interações de um dispositivo controlador de TV.
* **Atributos:** `ligada` (booleano), `volume_atual` e `canal_atual`.
* **Regra/Método:** * Ligar e desligar o aparelho.
    * Aumentar/Diminuir volume (com travas de limite mínimo de 0 e máximo de 100).
    * Mudar de canal (avançar/retroceder ou ir para um canal específico, validando se o canal é positivo).
    * *Regra de Ouro:* Bloquear qualquer alteração de volume ou canal se a TV estiver desligada.
"""