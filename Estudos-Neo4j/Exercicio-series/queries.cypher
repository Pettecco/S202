MATCH (n) return n

MATCH(p:Person)-[r]-(d:Dog) return p, d, r

MATCH(p:Person)-[:FAZ_PARTE]->(s:Serie{nome:'Scooby Doo'})
WHERE p.sexo = 'F' return p

MATCH (p:Person)-[:FAZ_PARTE]->(s:Serie)
WHERE NOT s.nome CONTAINS p.nome
RETURN p.nome, s.nome

MATCH(c:Company) WHERE 'Pixar' in c.subsidiarias SET c.fundador = 'Walter Elias Disney'
