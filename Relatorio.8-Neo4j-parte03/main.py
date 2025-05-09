from database import Database
from GameDatabase import GameDatabase

# Função para deixar o print mais claro/visivel
def print_match_info(match):
    print(f"Partida ID: {match['id']}")
    print(f"Resultado: {match['result']}")
    print(f"Jogadores: {', '.join(match['players'])}")
    print("-" * 40)


db = Database("bolt://localhost:7687", "neo4j", "neo4jneo4j")
db.drop_all()

game_db = GameDatabase(db)

# Criar jogadores
game_db.create_player("Petterson")
game_db.create_player("João")
game_db.create_player("Gabriel")
game_db.create_player("Thales")

# Listar jogadores para pegar IDs
players = game_db.get_players()
petterson_id = players[0]["id"]
joao_id = players[1]["id"]
gabriel_id = players[2]["id"]
thales_id = players[3]["id"]

# Criar uma partida
game_db.create_match([petterson_id, joao_id], "Petteson foi o vencedor")
game_db.create_match([gabriel_id, thales_id], "Thales foi o vencedor")

# Pega partidas de um jogador
petterson_matches = game_db.get_player_matches(petterson_id)
gabriel_matches = game_db.get_player_matches(gabriel_id)

# Pegando informações de uma partida
first_match_info = game_db.get_match(petterson_matches[0]["match_id"])
second_match_info = game_db.get_match(gabriel_matches[0]["match_id"])

print_match_info(first_match_info)
print_match_info(second_match_info)

# Atualizar nome de um jogador 
game_db.update_player(petterson_id, "Petterson Sousa")
players = game_db.get_players()
print("Jogadores após atualização:")
for p in players:
    print(f"- {p['name']} (ID: {p['id']})")
print("-" * 40)

# Excluir um jogador
game_db.delete_player(gabriel_id)
players = game_db.get_players()
print("Jogadores após exclusão:")
for p in players:
    print(f"- {p['name']} (ID: {p['id']})")
print("-" * 40)

db.close()
