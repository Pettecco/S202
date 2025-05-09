from uuid import uuid4

class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {id: $id, name: $name})"
        parameters = {"id": str(uuid4()), "name": name}
        self.db.execute_query(query, parameters)

    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player {id: $id}) SET p.name = $name"
        parameters = {"id": player_id, "name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_id):
        query = "MATCH (p:Player {id: $id}) DETACH DELETE p"
        parameters = {"id": player_id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.id AS id, p.name AS name"
        results = self.db.execute_query(query)
        return [{"id": r["id"], "name": r["name"]} for r in results]

    def create_match(self, player_ids, result):
        match_id = str(uuid4())
        query = """
        CREATE (m:Match {id: $id, result: $result})
        WITH m
        UNWIND $player_ids AS pid
        MATCH (p:Player {id: pid})
        CREATE (p)-[:PARTICIPOU]->(m)
        """
        parameters = {"id": match_id, "player_ids": player_ids, "result": result}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $id}) DETACH DELETE m"
        parameters = {"id": match_id}
        self.db.execute_query(query, parameters)

    def get_match(self, match_id):
        query = """
        MATCH (p:Player)-[:PARTICIPOU]->(m:Match {id: $id})
        RETURN m.id AS id, m.result AS result, collect(p.name) AS players
        """
        parameters = {"id": match_id}
        result = self.db.execute_query(query, parameters)
        return result[0] if result else None

    def get_player_matches(self, player_id):
        query = """
        MATCH (p:Player {id: $id})-[:PARTICIPOU]->(m:Match)
        RETURN m.id AS match_id, m.result AS result
        """
        parameters = {"id": player_id}
        results = self.db.execute_query(query, parameters)
        return [{"match_id": r["match_id"], "result": r["result"]} for r in results]
