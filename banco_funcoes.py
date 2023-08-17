class Cliente:
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo
        
    def deposito(self, valor):
        self.saldo += valor
        
    def saque(self, valor):
        self.saldo -= valor
        
    def extrato(self, op):
        historico = []
        
        if op == self.saque():
            historico.append()
            
        
    def __str__(self):
        return f"Saldo em conta: R$ {self.saldo}"

class Conta:
    def __init__(self, conta, agencia, nome, cpf, data_nasc):
        self.conta = conta
        self.agencia = agencia
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        
    def criar_conta(self, conta, agencia, nome, cpf, data_nasc):
        