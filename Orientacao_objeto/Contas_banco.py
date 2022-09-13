class ContaCorrente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta() :
            print('Você não tem saldo suficiente para sacar essa valor.')
            self.consultar_saldo()
        else:
            self.saldo -= valor


#Programa
conta_victor = ContaCorrente('Victor', '111.222.333-44')

#Depositando dinheiro
conta_victor.depositar(10000)
conta_victor.consultar_saldo()

#sacar dinheiro
conta_victor.sacar_dinheiro(10500)

print('Saldo final:')
conta_victor.consultar_saldo()

