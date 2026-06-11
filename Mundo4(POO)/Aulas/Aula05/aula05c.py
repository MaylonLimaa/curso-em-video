class ContaBancaria:
    """
    Classe que representa uma conta bancária simples.
    Permite criar uma conta, verificar os dados, sacar e depositar.
    """

    def __init__(self, titular, id_conta, saldo=0):
        """Método construtor da ContaBancaria.

        Args:
            titular (string): Nome do titular
            id_conta (string): ID da Conta.
            saldo (float, optional): Saldo da conta. Defaults to 0.
        """
        self.titular = titular
        self.saldo = saldo
        self.id_conta = id_conta

    def depositar(self, valor):
        """Deposita um valor na conta

        Args:
            valor (float): Valor a ser depositado
        """
        self.saldo += valor

    def sacar(self, valor):
        """Saca um valor da conta

        Args:
            valor (float): Valor a ser sacado.
        """
        self.saldo -= valor

    def __str__(self):
        """Método de apresentação do objeto.

        Returns:
            string: Texto formatado com o ID da conta, nome do titular e saldo da conta.
        """
        return f'A conta {self.id_conta} de {self.titular} possui R$ {self.saldo:.2f} de saldo'

c1 = ContaBancaria('Maylon', '001', 1900)
print(c1)
