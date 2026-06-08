# 🚀 Desafios de Programação Orientada a Objetos (POO)

Uma coleção de desafios práticos para treinar os pilares da Programação Orientada a Objetos, focando na criação de classes, encapsulamento de regras de negócio e integridade dos dados.

---

### 📋 Lista de Desafios

#### 👤 Desafio 16: Classe Funcionário ✅ 
* **Objetivo:** Criar uma classe para cadastrar as informações básicas de um colaborador.
* **Atributos:** `nome`, `setor` e `cargo`.
* **Regra/Método:** Um método que retorne uma string de apresentação com os dados do funcionário (ex: *"Olá, meu nome é [Nome], trabalho no setor de [Setor] como [Cargo]"*).

#### 🏷️ Desafio 17: Classe Produto ✅ 
* **Objetivo:** Gerenciar as informações de precificação de itens.
* **Atributos:** `nome` e `preco`.
* **Regra/Método:** Um método que monte e retorne uma string formatada simulando uma etiqueta de preço (ex: *"[Produto] - R$ [Preço]"* com duas casas decimais).

#### 🥩 Desafio 18: Classe Churrasco ✅ 
* **Objetivo:** Criar uma calculadora para gerenciar os custos e insumos de um evento.
* **Atributos:** Preço fixo por quilo da carne (definido na instância).
* **Regra/Método:** Receber o número de pessoas e calcular:
    * A quantidade total de carne necessária (baseada em um consumo de 400g por pessoa).
    * O custo total da carne.
    * O valor rateado por pessoa.
    * *Nota: O método deve retornar esses dados estruturados (ou em formato de texto descritivo) para que o programa principal decida como exibir.*

#### 📖 Desafio 19: Classe Livro 🔄
* **Objetivo:** Simular o comportamento de leitura de uma obra física.
* **Atributos:** `titulo`, `total_paginas` e `pagina_atual` (iniciando em 0 ou 1).
* **Regra/Método:** Um método para avançar páginas. Deve validar se a nova página não ultrapassa o `total_paginas` e retornar um aviso/status caso o leitor atinja o final do livro.

#### 🎮 Desafio 20: Classe Gamer 🔄
* **Objetivo:** Montar a ficha de perfil de um jogador.
* **Atributos:** `nome`, `nick` e uma lista (`list`) de jogos favoritos.
* **Regra/Método:** Um método que retorne a ficha completa do jogador, garantindo que a lista de jogos favoritos seja apresentada organizada em **ordem alfabética**.

#### 🖊️ Desafio 21: Classe Caneta 🔄
* **Objetivo:** Controlar o estado e o funcionamento de um objeto simples.
* **Atributos:** `cor` (permitir estritamente apenas `azul`, `vermelha` ou `verde`) e `tampada` (booleano).
* **Regra/Método:** Métodos para tampar/destampar e um método para simular a escrita. A classe deve validar: se tentar escrever com a caneta tampada, ela deve retornar uma mensagem de erro ou impedir a ação.

#### 📺 Desafio 22: Classe Controle Remoto 🔄
* **Objetivo:** Modelar as interações de um dispositivo controlador de TV.
* **Atributos:** `ligada` (booleano), `volume_atual` e `canal_atual`.
* **Regra/Método:** * Ligar e desligar o aparelho.
    * Aumentar/Diminuir volume (com travas de limite mínimo de 0 e máximo de 100).
    * Mudar de canal (avançar/retroceder ou ir para um canal específico, validando se o canal é positivo).
    * *Regra de Ouro:* Bloquear qualquer alteração de volume ou canal se a TV estiver desligada.
