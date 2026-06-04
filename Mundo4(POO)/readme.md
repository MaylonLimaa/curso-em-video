# 📝 Gerenciador de Tarefas (Task Manager)

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![POO](https://img.shields.io/badge/Paradigma-Orientado%20a%20Objetos-green)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)]()

O **Gerenciador de Tarefas** é um sistema de linha de comando (CLI) desenvolvido em Python para praticar e consolidar conceitos fundamentais de **Programação Orientada a Objetos (POO)**. O foco principal deste projeto foi aplicar os pilares do encapsulamento, separação de responsabilidades e a correta troca de mensagens entre objetos.

---

## 🎯 Funcionalidades

- [x] **Criar Tarefas**: Instanciação de tarefas com Título e Descrição.
- [x] **Adicionar ao Gerenciador**: Armazenamento dinâmico de tarefas através de composição/associação.
- [ ] **Iniciar Tarefa**: Alterar o estado interno da tarefa para `"Em andamento"`.
- [ ] **Concluir Tarefa**: Marcar o estado como `"Concluída"` através de métodos controlados.
- [ ] **Listar Tarefas**: Exibir no terminal o ID (índice da lista) e os detalhes de cada tarefa.
- [ ] **Remover Tarefa**: Eliminar uma tarefa do sistema usando o seu ID.

---

## 🧠 Conceitos de POO Aplicados

Durante o desenvolvimento, as seguintes boas práticas de arquitetura de software foram aplicadas:

1. **Encapsulamento Estrito**: O atributo `__status` da classe `Tarefa` e `__tarefas` do `Gerenciador` foram definidos como privados. O mundo externo não altera estes dados diretamente.
2. **Troca de Mensagens (Message Passing)**: O `Gerenciador` não invade o escopo da `Tarefa`. Ele apenas envia um pedido (chama um método público da tarefa) para que ela altere o seu próprio estado.
3. **Uso de Properties (`@property`)**: Implementação de getters controlados em Python para expor dados de forma segura, eliminando a necessidade de setters desnecessários que quebrariam a lógica de negócio.

---

## 🏗️ Estrutura das Classes

O projeto está dividido em duas entidades principais que se comunicam de forma harmoniosa:

### 1. Classe `Tarefa`
Responsável por moldar as características e comportamentos de uma tarefa individual.
- **Atributos**: `titulo` (público), `descricao` (público), `__status` (privado).
- **Estados Possíveis**: `"Pendente"` (padrão), `"Em andamento"`, `"Concluída"`.

### 2. Classe `Gerenciador`
O maestro do sistema, responsável por coordenar a coleção de tarefas.
- **Atributos**: `__tarefas` (lista privada).
- **Métodos**: `addTarefa()`, `iniciarTarefa()`, `concluirTarefa()`, `removerTarefa()`.

---

## 🛠️ Como Executar o Projeto

### Pré-requisitos
Ter o Python 3.10 ou superior instalado na tua máquina.

### Passo a Passo
1. Clona este repositório para a tua máquina local:
   ```bash
   git clone [https://github.com/MaylonLimaa/curso-em-video-python.git](https://github.com/MaylonLimaa/curso-em-video-python.git)