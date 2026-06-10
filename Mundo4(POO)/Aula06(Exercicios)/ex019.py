"""#### 📖 Desafio 19: Classe Livro
* **Objetivo:** Simular o comportamento de leitura de uma obra física.
* **Atributos:** `titulo`, `total_paginas` e `pagina_atual` (iniciando em 0 ou 1).
* **Regra/Método:** Um método para avançar páginas. Deve validar se a nova página não ultrapassa o `total_paginas` e retornar um aviso/status caso o leitor atinja o final do livro.
"""

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 0

    def avancar_paginas(self, paginas):
        nova_pagina = self.pagina_atual + paginas

        if nova_pagina > self.total_paginas:
            return "Erro: Ultrapassa o total de páginas."

        self.pagina_atual = nova_pagina

        if self.pagina_atual == self.total_paginas:
            return "Você chegou ao fim do livro!"

        return f"Página atual: {self.pagina_atual}"


# Execução direta
meu_livro = Livro("Padrões de Projeto", 150)
print(meu_livro.avancar_paginas(50))
print(meu_livro.avancar_paginas(110))
print(meu_livro.avancar_paginas(100))
