CREATE 
  (:Pessoa:Jornalista:Comunicação {nome: "Donizete", idade: 57, sexo: "M"}),
  (:Pessoa:Pedagoga {nome: "Celia", idade: 56, sexo: "F"}),
  (:Pessoa:Publicitario:Comunicação {nome: "Patrick", idade: 27, sexo: "M"}),
  (:Pessoa:Engenheiro {nome: "Petterson", idade: 22, sexo: "M"}),
  (:Pessoa:Engenheiro {nome: "Camila", idade: 22, sexo: "F"}),
  (:Pessoa:ProdutorRural {nome: "Daura", idade: 84, sexo: "F"}),
  (:Pessoa:ProdutorRural {nome: "Nico", idade: 87, sexo: "M"}),
  (:Pessoa:ProdutorRural {nome: "Isael", idade: 60, sexo: "M"}),
  (:Pessoa:Mecanico {nome: "Juraci", idade: null, sexo: "M"}),
  (:Pessoa:Arquiteto {nome: "Giovana", idade: 25, sexo: "F"}),
  (:Pessoa:Cachorro {nome: "Buddy", idade: 2, sexo: "M"}),
  (:Pessoa:Policial {nome: "Juraci Pereira", idade: 83, sexo: "M"}),
  (:FuncionariaPublica:Pessoa {nome: "Maria Helena", idade: 80, sexo: "F"}),
  (:FuncionariaPublica:Pessoa {nome: "Selma", idade: 58, sexo: "F"})

WITH 1 AS dummy 
MATCH (daura:Pessoa {nome: "Daura"})
MATCH (nico:Pessoa {nome: "Nico"})
MATCH (celia:Pessoa {nome: "Celia"})
MATCH (donizete:Pessoa {nome: "Donizete"})
MATCH (patrick:Pessoa {nome: "Patrick"})
MATCH (giovana:Pessoa {nome: "Giovana"})
MATCH (petterson:Pessoa {nome: "Petterson"})
MATCH (camila:Pessoa {nome: "Camila"})
MATCH (isael:Pessoa {nome: "Isael"})
MATCH (juraci:Pessoa {nome: "Juraci"})
MATCH (juraciPereira:Pessoa {nome: "Juraci Pereira"})
MATCH (mariaHelena:Pessoa {nome: "Maria Helena"})
MATCH (selma:Pessoa {nome: "Selma"})
MATCH (buddy:Pessoa {nome: "Buddy"})

CREATE (daura)-[:CASADO_COM]->(nico)
CREATE (nico)-[:CASADO_COM]->(daura)

CREATE (celia)-[:CASADO_COM {anos: 30}]->(donizete)
CREATE (donizete)-[:CASADO_COM {anos: 30}]->(celia)

CREATE (patrick)-[:NAMORA_COM]->(giovana)
CREATE (giovana)-[:NAMORA_COM]->(patrick)

CREATE (petterson)-[:NAMORA_COM {meses: 6}]->(camila)
CREATE (camila)-[:NAMORA_COM {meses: 6}]->(petterson)

CREATE (isael)-[:IRMAO_DE]->(donizete)
CREATE (donizete)-[:IRMAO_DE]->(isael)

CREATE (patrick)-[:IRMAO_DE]->(petterson)
CREATE (petterson)-[:IRMAO_DE]->(patrick)

CREATE (celia)-[:IRMAO_DE]->(juraci)
CREATE (juraci)-[:IRMAO_DE]->(celia)

CREATE (daura)-[:PAI_DE]->(donizete)
CREATE (nico)-[:PAI_DE]->(donizete)

CREATE (celia)-[:PAI_DE]->(petterson)
CREATE (donizete)-[:PAI_DE]->(petterson)

CREATE (celia)-[:PAI_DE]->(patrick)
CREATE (donizete)-[:PAI_DE]->(patrick)

CREATE (giovana)-[:DONO_DE]->(buddy);

CREATE (mariaHelena)-[:CASADO_COM]->(juraciPereira)
CREATE (juraciPereira)-[:CASADO_COM]->(mariaHelena)

CREATE (mariaHelena)-[:PAI_DE]->(celia)
CREATE (juraciPereira)-[:PAI_DE]->(celia)

CREATE (mariaHelena)-[:PAI_DE]->(selma)
CREATE (juraciPereira)-[:PAI_DE]->(selma)

CREATE (mariaHelena)-[:PAI_DE]->(juraci)
CREATE (juraciPereira)-[:PAI_DE]->(juraci)

CREATE (celia)-[:IRMAO_DE]->(selma)
CREATE (selma)-[:IRMAO_DE]->(celia)

CREATE (celia)-[:IRMAO_DE]->(juraci)
CREATE (juraci)-[:IRMAO_DE]->(celia)

CREATE (selma)-[:IRMAO_DE]->(juraci)
CREATE (juraci)-[:IRMAO_DE]->(selma)
