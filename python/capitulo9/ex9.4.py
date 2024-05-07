class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_disponivel, valor_solicitado):
        super().__init__("Saldo insuficiente para realizar o saque de R$ {:.2f}. Saldo disponível: R$ {:.2f}".format(valor_solicitado, saldo_disponivel))
        self.saldo_disponivel = saldo_disponivel
        self.valor_solicitado = valor_solicitado

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de R$ {:.2f} realizado com sucesso.".format(valor))

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
        else:
            raise SaldoInsuficienteError(self.saldo, valor)

conta = ContaBancaria(1000)

try:
    conta.sacar(1200)
except SaldoInsuficienteError as e:
    print(e)

print("Saldo atual:", conta.saldo)
