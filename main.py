import datetime

class Usuario:
    def __init__(self, user_id, nome):
        self.user_id = user_id
        self.nome = nome

class ContaCorrente:
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0
        self.limite_diario = 1500
        self.numero_saque = 0
        self.ultima_data_saque = None
        self.saques = []
        self.depositos = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
        else:
            print(f'O Valor do depósito não pode ser negativo ou nulo')
        print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')

    def saque(self, valor):
        hoje = datetime.date.today()

        if self.ultima_data_saque != hoje:
            self.limite_diario = 1500
            self.ultima_data_saque = hoje
            self.numero_saque = 0

        if valor <= self.saldo and valor <= self.limite_diario and self.numero_saque < 3 and valor < 500:
            self.saldo -= valor
            self.limite_diario -= valor
            self.numero_saque += 1
            self.saques.append(valor)
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')
        elif valor > self.limite_diario:
            print('Limite diário de saque excedido. Máximo permitido: R$1500')
        elif valor > 500:
            print('Limite máximo por saque de R$ 500,00')
        elif valor > self.saldo:
            print('Saldo indisponível')
        else:
            print('Máximo de 3 saques por dia excedidos.')

    def extrato(self):
        print(f'Saldo atual: R${self.saldo:.2f}')
        print(f'Depósitos: {[f"R$ {deposito:.2f}" for deposito in self.depositos]}')
        print(f'Saques: {[f"R$ {saque:.2f}" for saque in self.saques]}')

class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.contas_correntes = []

    def criar_usuario(self, user_id, nome):
        usuario = Usuario(user_id, nome)
        self.usuarios.append(usuario)
        print(f'Usuário {nome} criado com sucesso!')

    def criar_conta_corrente(self, user_id):
        usuario = next((user for user in self.usuarios if user.user_id == user_id), None)
        if usuario:
            conta_corrente = ContaCorrente(usuario)
            self.contas_correntes.append(conta_corrente)
            print(f'Conta corrente criada para o usuário {usuario.nome} com sucesso!')
        else:
            print(f'Usuário com ID {user_id} não encontrado.')

    def get_conta_corrente(self, user_id):
        return next((conta for conta in self.contas_correntes if conta.usuario.user_id == user_id), None)


def main():
    sistema_bancario = SistemaBancario()

    while True:
        print("\nEscolha uma opção:")
        print("1. Criar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Depósito")
        print("4. Saque")
        print("5. Extrato")
        print("0. Sair")

        escolha = int(input("Digite o número da opção desejada: "))

        if escolha == 1:
            user_id = int(input("Digite o ID do usuário: "))
            nome = input("Digite o nome do usuário: ")
            sistema_bancario.criar_usuario(user_id, nome)
        elif escolha == 2:
            user_id = int(input("Digite o ID do usuário para criar a conta corrente: "))
            sistema_bancario.criar_conta_corrente(user_id)
        elif escolha == 3:
            user_id = int(input("Digite o ID do usuário: "))
            conta_corrente = sistema_bancario.get_conta_corrente(user_id)
            if conta_corrente:
                valor_deposito = float(input("Digite o valor do depósito: "))
                conta_corrente.deposito(valor_deposito)
            else:
                print("Conta corrente não encontrada para o usuário.")
        elif escolha == 4:
            user_id = int(input("Digite o ID do usuário: "))
            conta_corrente = sistema_bancario.get_conta_corrente(user_id)
            if conta_corrente:
                valor_saque = float(input("Digite o valor do saque: "))
                conta_corrente.saque(valor_saque)
            else:
                print("Conta corrente não encontrada para o usuário.")
        elif escolha == 5:
            user_id = int(input("Digite o ID do usuário: "))
            conta_corrente = sistema_bancario.get_conta_corrente(user_id)
            if conta_corrente:
                conta_corrente.extrato()
            else:
                print("Conta corrente não encontrada para o usuário.")
        elif escolha == 0:
            print("Sistema encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
