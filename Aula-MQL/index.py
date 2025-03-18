# Exercícios sobre MQL
from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')

db = client['dbworld']

paises = db.countries

results = paises.find()

for aux in results:
  pprint.pprint(aux)

# Mostre apenas o nome oficial dos países que são da região "Americas" e possues área menor que 100
results = paises.find({"region": "Americas", "area": {"$lt": 100}}, {"name.common": 1})

for aux in results:
  pprint.pprint(aux)

# Mostre o nome comum, a latitude e longitude apenas dos países que falam português (por)

results = paises.find({"languages.por": "Portuguese"}, {"name.common": 1, "latlng": 1})

for aux in results:
  pprint.pprint(aux)

# Mostre apenas o nome comum dos países que começam com 'B' e ordene os resultados por ordem crescente de area

results = paises.find({"name.common": {"$regex": "^B"}}, {"name.common": 1}).sort("area", 1)

for aux in results:
  pprint.pprint(aux)