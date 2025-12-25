def leiaDinheiro(txt):
    """
    Função para validar um input
    """
    while True:
        n = input(txt).replace(',', '.').strip() # Troca vírgula por ponto
        # Verifica se sobrou algo que não é número (desconsiderando o ponto)
        if n.isalpha() or n == '':
            print(f'{n} é um preço inválido!')
        else:
            return float(n)
