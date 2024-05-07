class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de R$ {:.2f} realizado com sucesso.".format(valor))

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
        else:
            print("Saldo insuficiente para saque.")

    def consultar_saldo(self):
        print("Saldo atual: R$ {:.2f}".format(self.saldo))


class ContaPoupanca(ContaBancaria):
    def __init__(self, taxa_juros):
        super().__init__()
        self.taxa_juros = taxa_juros

    def rendimento(self, num_meses):
        for _ in range(num_meses):
            self.saldo *= (1 + self.taxa_juros / 100)
        print("Rendimento após {} meses: R$ {:.2f}".format(num_meses, self.saldo))


conta_poupanca = ContaPoupanca(0.5)

conta_poupanca.depositar(1000)

conta_poupanca.rendimento(12)
