MATCH (n) RETURN n;

MATCH (g:Game) WHERE g.ano > 2012 RETURN g;

MATCH (g:Game) WHERE g.genero = 'Terror' RETURN g;

MATCH (j:Jurado)-[r:JOGOU]->(g:Game)
WHERE r.nota >= 7
RETURN g, r.nota;

