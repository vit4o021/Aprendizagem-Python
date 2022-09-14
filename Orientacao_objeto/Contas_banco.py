from datetime import datetime
import pytz


class ContaCorrente:

    @staticmethod # --> sinalização para indicar que é um método estático/auxiliar
    def _data_hora(): #método estático --> é um método que não vai usar nada da classe. Logo, não precisa de self
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta) :
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self): # --> O "_" na frente significa que é um método que não é para ser usado dentro do programa
        self.limite = -1000  # e sim como um auxiliar para outros métodos.
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta() :
            print('Você não tem saldo suficiente para sacar essa valor.')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_cheque_especial(self):
        print('Seu limite de cheque especial é de R${:,.2f}.'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de transações: ')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


#Programa
conta_victor = ContaCorrente('Victor', '111.222.333-44', 1234, 34062)

#Depositando dinheiro
conta_victor.depositar(10000)
conta_victor.consultar_saldo()

#sacar dinheiro
#conta_victor.sacar_dinheiro(10500)

print('Saldo final:')
conta_victor.consultar_saldo()

conta_victor.consultar_limite_cheque_especial()

print('-' * 20)
print('Valor, Saldo, Data e hora')
conta_victor.consultar_historico_transacoes()

print('-' * 20)
conta_mae_victor = ContaCorrente('Veronica', '555.666.777-88', 5678, 34532)
conta_victor.transferir(1000, conta_mae_victor)

conta_victor.consultar_saldo()
conta_mae_victor.consultar_saldo()

conta_victor.consultar_historico_transacoes()
conta_mae_victor.consultar_historico_transacoes()