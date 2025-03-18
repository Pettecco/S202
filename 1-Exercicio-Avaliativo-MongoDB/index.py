import threading
import time
import random
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['bancoiot']

sensores = db.sensores

novoSensor1 = {
  "nomeSensor": "Temp1",
  "valorSensor": '', 
  "unidadeMedida": 'Cº',
  "sensorAlarmado": False
}

novoSensor2 = {
  "nomeSensor": "Temp2",
  "valorSensor": '', 
  "unidadeMedida": 'Cº',
  "sensorAlarmado": False
}

novoSensor3 = {
  "nomeSensor": "Temp3",
  "valorSensor": '', 
  "unidadeMedida": 'Cº',
  "sensorAlarmado": False
}

docs = [novoSensor1, novoSensor2, novoSensor3]

for i in docs:
  result = db.sensores.insert_one(i)

def sensor1_dados(nome, intervalo):
  valor = 0
  while valor < 38:
    valor = random.randrange(30, 40)
    print(f"{nome} temperatura: {valor}")
    time.sleep(intervalo)
    sensores.find_one_and_update(
      {"nomeSensor": "Temp1"},
      {"$set": {"valorSensor": valor}}
    )
  sensores.find_one_and_update(
    {"nomeSensor": "Temp1"}, 
    {"$set": {"sensorAlarmado": True}}
  )
  print("Atenção! Temperatura muito alta! Verificar Sensor 1")


def sensor2_dados(nome, intervalo):
  valor = 0
  while valor < 38:
    valor = random.randrange(30, 40)
    print(f"{nome} temperatura: {valor}")
    time.sleep(intervalo)
    sensores.find_one_and_update(
      {"nomeSensor": "Temp2"},
      {"$set": {"valorSensor": valor}}
    )
  sensores.find_one_and_update(
    {"nomeSensor": "Temp2"}, 
    {"$set": {"sensorAlarmado": True}}
  )
  print("Atenção! Temperatura muito alta! Verificar Sensor 2")
 
  
def sensor3_dados(nome, intervalo):
  valor = 0
  while valor < 38:
    valor = random.randrange(30, 40)
    print(f"{nome} temperatura: {valor}")
    time.sleep(intervalo)
    sensores.find_one_and_update(
      {"nomeSensor": "Temp3"},
      {"$set": {"valorSensor": valor}}
    )
  sensores.find_one_and_update(
    {"nomeSensor": "Temp3"}, 
    {"$set": {"sensorAlarmado": True}}
  )
  print("Atenção! Temperatura muito alta! Verificar Sensor 3")

sensor1 = threading.Thread(target=sensor1_dados, args=("Sensor 1:", 2))
sensor2 = threading.Thread(target=sensor2_dados, args=("Sensor 2:", 2))
sensor3 = threading.Thread(target=sensor3_dados, args=("Sensor 3:", 2))
sensor1.start()
sensor2.start()
sensor3.start()