from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
# db.resetDatabase() 

def getAllEvolutionsOfAPokemonByName(name: str):
    return db.collection.find(
    {"name": name},
    {"name": 1, "next_evolution": 1} 
)

def getAllPokemonsWithEggsEqual5km():
    return db.collection.find({"egg": "5 km"})

def getPokemonsInIdInterval(id1: int, id2: int):
    return db.collection.find({"id": {"$gte": id1, "$lte": id2}}, {"id": 1, "name": 1})


def getPokemonsTypeWaterAndWeaknessesPsychic():
    return db.collection.find({"type": {"$in": ["Water"]}, "weaknesses": {"$in": ["Psychic"]}})

def getPokemonsWithoutEvolution():
    return db.collection.find({"next_evolution": {"$exists": False}, "prev_evolution": {"$exists": False}})

pokemon_evolutions = getAllEvolutionsOfAPokemonByName("Charmander")
writeAJson(pokemon_evolutions, "pokemons_evolution_get_by_name")

pokemon_eggs = getAllPokemonsWithEggsEqual5km()
writeAJson(pokemon_eggs, "pokemons_with_egg_equal_5km")

pokemons_in_interval = getPokemonsInIdInterval(20, 100)
writeAJson(pokemons_in_interval, "pokemons_in_id_interval")

pokemons_type_water_and_weak_against_psychic = getPokemonsTypeWaterAndWeaknessesPsychic()
writeAJson(pokemons_type_water_and_weak_against_psychic, "pokemons_type_water_and_weak_against_psychic")

pokemons_without_evolution = getPokemonsWithoutEvolution()
writeAJson(pokemons_without_evolution, "pokemons_without_evolution")