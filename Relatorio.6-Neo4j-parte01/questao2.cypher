CREATE(:Game {titulo:'Persona 5', genero:'JRPG', ano:2017});
CREATE(:Game {titulo:'Valorant', genero:'Shooter', ano:2020});
CREATE(:Game {titulo:'Stardew Valley', genero:'Simulação', ano:2016});
CREATE(:Game {titulo:'The Sims 4', genero:'Simulação', ano:2014});

CREATE(:Jurado {nome:'Petterson'});
CREATE(:Jurado {nome:'Camila'});
CREATE(:Jurado {nome:'Matheus'});

MATCH (j:Jurado {nome:'Petterson'}), (g:Game {titulo:'Persona 5'})
CREATE (j)-[:JOGOU {nota:10, horas:320}]->(g);

MATCH (j:Jurado {nome:'Petterson'}), (g:Game {titulo:'Stardew Valley'})
CREATE (j)-[:JOGOU {nota:9, horas:70}]->(g);

MATCH (j:Jurado {nome:'Camila'}), (g:Game {titulo:'The Sims 4'})
CREATE (j)-[:JOGOU {nota:9, horas:500}]->(g);

MATCH (j:Jurado {nome:'Camila'}), (g:Game {titulo:'Stardew Valley'})
CREATE (j)-[:JOGOU {nota:7, horas:70}]->(g);

MATCH (j:Jurado {nome:'Matheus'}), (g:Game {titulo:'Valorant'})
CREATE (j)-[:JOGOU {nota:10, horas:2000}]->(g);

MATCH (j:Jurado {nome:'Matheus'}), (g:Game {titulo:'Stardew Valley'})
CREATE (j)-[:JOGOU {nota:9, horas:300}]->(g);

