from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista):
        try:
            corridas_formatadas = []
            for corrida in motorista.corridas:
                corrida_dict = {
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "Passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                }
                corridas_formatadas.append(corrida_dict)
            motorista_dict = {
                "nota": motorista.nota,
                "Corridas": corridas_formatadas
            }
            result = self.db.collection.insert_one(motorista_dict)
            print("Motorista inserido com sucesso no MongoDB!")
            print(f"ID do documento inserido: {result.inserted_id}")
        except Exception as e:
            print(f"Ocorreu um erro ao criar um motorista: {e}")
            return None

    def read_motorista(self, id: str):
      try:
        motorista = self.db.collection.find_one({"_id": ObjectId(id)})
        if motorista:
            print("Motorista encontrado:")
            print(f"Nota: {motorista['nota']}")
            print("Corridas:")
            for i, corrida in enumerate(motorista["Corridas"], start=1):
                print(f"Corrida {i}:")
                print(f"Nota: {corrida['nota']}")
                print(f"Distância: {corrida['distancia']}")
                print(f"Valor: {corrida['valor']}")
                passageiro = corrida["Passageiro"]
                print(f"Passageiro: {passageiro['nome']} - {passageiro['documento']}")
        else:
            print("Motorista não encontrado.")
      except Exception as e:
        print(f"Ocorreu um erro ao tentar buscar motorista: {e}")
        return None

    def update_motorista(self, id: str, motorista):
        try:
            corridas_formatadas = []
            for corrida in motorista.corridas:
                corrida_dict = {
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "Passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                }
                corridas_formatadas.append(corrida_dict)
            motorista_dict = {
                "nota": motorista.nota,
                "Corridas": corridas_formatadas
            }
            result = self.db.collection.update_one(
                {"_id": ObjectId(id)},  
                {"$set": motorista_dict}  
            )

            if result.modified_count == 1:
                print("Motorista atualizado com sucesso!")
            else:
                print("Nenhum motorista encontrado ou nada foi alterado.")
            
            return result.modified_count

        except Exception as e:
            print(f"Ocorreu um erro ao tentar atualizar o motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count == 1:
                print("Motorista deletado com sucesso!")
            else:
                print("Nenhum motorista encontrado com esse ID.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar deletar o motorista: {e}")
            return None
