---

# Guia de Estudo: Docstrings (Google vs Sphinx)

As docstrings servem para documentar o que uma função, classe ou módulo faz. Quando o seu código cresce, apenas ler o nome da função não basta; você precisa entender rapidamente o que ela espera receber, o que ela faz e o que ela devolve.

## 📌 O que compõe uma boa Docstring?

Uma docstring de alta qualidade deve responder a três perguntas principais:

1. **O que** a função/classe faz?
2. **Quais argumentos** ela recebe (e de que tipo)?
3. **O que** ela retorna?

---

## ⚖️ Os Dois Principais Estilos do Mercado

### 1. Estilo Google (Google Style)

* **Filosofia:** Focado totalmente na **legibilidade humana** e na simplicidade. É um visual limpo diretamente no editor.
* **Estrutura:** Usa títulos diretos e amigáveis seguidos por dois pontos (como `Args:`, `Returns:`, `Raises:`). O conteúdo de cada seção fica recuado com uma tabulação.
* **Tipagem:** Os tipos de dados (como texto ou número) são colocados discretamente entre parênteses ao lado do nome da variável.
* **Uso ideal:** No dia a dia, em projetos pessoais, estudos ou equipes dinâmicas no VS Code por ser muito ágil.

### 2. Estilo Sphinx (reStructuredText)

* **Filosofia:** Focado na **automação** e em geradores de documentação.
* **Estrutura:** Usa marcadores técnicos (etiquetas) que começam com dois pontos, como `:param ...:` e `:return:`.
* **Tipagem:** Os tipos ganham linhas ou tags próprias isoladas (`:type:` e `:rtype:`), o que deixa o texto mais poluído para humanos, mas perfeito para máquinas.
* **Uso ideal:** Quando você vai criar um módulo público ou biblioteca gigante (como o *Pandas* ou o *NumPy*) que depois precisa ser transformado em um site de documentação web automaticamente.

---

## 💻 Exemplos Práticos Comparativos

### Versão 1: Estilo Google (Foco na Leitura Humana)

```python
class Calculadora:
    """Uma classe simples para realizar operações matemáticas básicas."""

    def somar(self, primeiro_numero, segundo_numero):
        """Calcula a soma de dois números fornecidos.

        Args:
            primeiro_numero (int, float): O primeiro valor numérico.
            segundo_numero (int, float): O segundo valor numérico.

        Returns:
            int, float: O resultado da soma dos dois números.
        """
        return primeiro_numero + segundo_numero

    def subtrair(self, primeiro_numero, segundo_numero):
        """Calcula a diferença entre o primeiro e o segundo número.

        Args:
            primeiro_numero (int, float): O valor do qual será subtraído.
            segundo_numero (int, float): O valor a ser subtraído.

        Returns:
            int, float: O resultado da subtração.
        """
        return primeiro_numero - segundo_numero

```

### Versão 2: Estilo Sphinx (Foco em Geradores Web)

```python
class Calculadora:
    """Uma classe simples para realizar operações matemáticas básicas."""

    def somar(self, primeiro_numero, segundo_numero):
        """Calcula a soma de dois números fornecidos.

        :param primeiro_numero: O primeiro valor numérico.
        :type primeiro_numero: int, float
        :param segundo_numero: O segundo valor numérico.
        :type segundo_numero: int, float
        :return: O resultado da soma dos dois números.
        :rtype: int, float
        """
        return primeiro_numero + segundo_numero

    def subtrair(self, primeiro_numero, segundo_numero):
        """Calcula a diferença entre o primeiro e o segundo número.

        :param primeiro_numero: O valor do qual será subtraído.
        :type primeiro_numero: int, float
        :param segundo_numero: O valor a ser subtraído.
        :type segundo_numero: int, float
        :return: O resultado da subtração.
        :rtype: int, float
        """
        return primeiro_numero - segundo_numero

```

---

## 🛠️ Regra Prática para Seus Códigos

Para manter a agilidade e organização nos seus estudos cotidianos, adote esta anatomia padrão:

1. **Resumo curto** na primeira linha.
2. **Explicação adicional** somente se o código for muito complexo.
3. **Args:** para listar os parâmetros.
4. **Returns:** para detalhar o retorno.
5. **Raises:** se houver alguma exceção importante tratada.

*💡 Dica de ouro:* Combine isso com os **Type Hints** do Python (ex: `def somar(a: int, b: int) -> int:`) para evitar redigir tipos repetidos dentro do texto e manter tudo moderno.

---