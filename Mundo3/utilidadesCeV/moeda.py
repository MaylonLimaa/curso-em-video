"""
Este arquivo é referente: Ao Ex 111.
"""

class Moeda:
    """
    Classe Moeda - Está classe tem os metodos usados para o
    exercício 107.
    """
    @staticmethod
    def aumentar(vlr, aument, format=False):
        """
        Recebe um parametro do valor e ouro em % e aumenta o valor da moeda
        de acordo com a %
        Uso de staticmethod devido ao propósito do exercicio
        retorna o valor com o aumento
        """
        vlr += (aument / 100) * vlr
        if not format:
            return vlr
        else:
            return Moeda.moeda(vlr)

    @staticmethod
    def diminuir(vlr, reduc, format=False):
        """
        Recebe um parametro do valor e ouro em % e diminui o valor da moeda
        de acordo com a %
        Uso de staticmethod devido ao propósito do exercicio
        retorna o valor com o desconto
        """
        vlr -= (reduc/100) * vlr
        if not format:
            return vlr
        else:
            return Moeda.moeda(vlr)
    @staticmethod

    def dobro(vlr, format=False):
        """
        Recebe o parametro do valor e retorna o dobro
        """
        vlr *= 2
        if not format:
            return vlr
        else:
            return Moeda.moeda(vlr)

    @staticmethod
    def metade(vlr):
        """
        Recebe o paremetro do valor e retorna metade dele
        """
        vlr /= 2
        return vlr

    @staticmethod
    def moeda(vlr):
        """
        Método para formatar o valor
        """
        txt = f'O valor é R$ {vlr:,.2f}'
        return txt.replace(',', 'X').replace('.', ',').replace('X', '.')
    @staticmethod
    def resumo():
        """
        O método resumo informa sobre as funções que temos na classe Moeda
        """
        print('-' * 40)
        print(f'{"MANUAL DA CLASSE MOEDA":^40}')
        print('-' * 40)
        print('Método aumentar():')
        print(' - Recebe: vlr (float), aument (% em int/float), format (bool).')
        print(' - O que faz: Adiciona a porcentagem ao valor original.')
        
        print('\nMétodo diminuir():')
        print(' - Recebe: vlr (float), reduc (% em int/float), format (bool).')
        print(' - O que faz: Subtrai a porcentagem do valor original.')
        
        print('\nMétodo dobro() e metade():')
        print(' - Recebe: vlr (float), format (bool).')
        print(' - O que faz: Multiplica por 2 ou divide por 2 o valor.')
        
        print('\nMétodo moeda():')
        print(' - Recebe: vlr (float).')
        print(' - O que faz: Transforma o número em String formatada em R$.')
        print('-' * 40)
