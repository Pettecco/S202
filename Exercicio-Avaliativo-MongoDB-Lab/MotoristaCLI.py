from Corrida import Corrida
from Motorista import Motorista
from Passageiro import Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Digite um comando: ")
            if command == "quit":
                print("Programa encerrado!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente de novo.")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nome_passageiro = input("Digite o nome do passageiro: ")
        documento_passageiro = input("Digite o documento do passageiro: ")
        passageiro = Passageiro(nome_passageiro, documento_passageiro)
        qnt_corridas = int(input("Digite a quantidade de corridas que o passageiro utilizou: "))
        corridas = []
        for i in range(qnt_corridas):
            nota = int(input(f"Digite a nota da {i+1} corrida: "))
            distancia = float(input(f"Digite a distancia da {i+1} corrida: "))
            valor = float(input(f"Digite o valor da {i+1} corrida: "))
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)     
        motorista_nota = int(input("Digite a nota do motorista: "))
        motorista = Motorista(motorista_nota)
        motorista.corridas = corridas
        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):
        id = input("Insira o ID do motorista: ")
        self.motorista_model.read_motorista(id)

    def update_motorista(self):
        id = input("Insira o ID do motorista: ")
        nome_passageiro = input("Digite o novo nome do passageiro: ")
        documento_passageiro = input("Digite o novo documento do passageiro: ")
        passageiro = Passageiro(nome_passageiro, documento_passageiro)
        qnt_corridas = int(input("Digite a nova quantidade de corridas que o passageiro utilizou: "))
        corridas = []
        for i in range(qnt_corridas):
            nota = int(input(f"Digite a nota da {i+1} corrida: "))
            distancia = float(input(f"Digite a distancia da {i+1} corrida: "))
            valor = float(input(f"Digite o valor da {i+1} corrida: "))
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)     
        motorista_nota = int(input("Digite a nova nota do motorista: "))
        motorista = Motorista(motorista_nota)
        motorista.corridas = corridas
        self.motorista_model.update_motorista(id, motorista)

    def delete_motorista(self):
        id = input("Insira o ID do motorista: ")
        self.motorista_model.delete_motorista(id)
        
    def run(self):
        print("Welcome to the Motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        