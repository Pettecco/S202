from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def drop_database(tx):
    try:
        tx.run("MATCH(n) DETACH DELETE n;")
    except Exception:
        print("Erro ao excluir...")
        raise

def get_family(tx):
    query = """
        MATCH (n) RETURN DISTINCT(n.nome) AS nome;
    """
    try:
        result = tx.run(query)
        return [{
            'nome':row['nome']
        } for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def get_farmer(tx):
    query = """
      MATCH (f:ProdutorRural) RETURN DISTINCT(f.nome) AS nome
    """
    try:
        result = tx.run(query)
        return [{
            'nome':row['nome']
        } for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def get_comunicators(tx):
    query = """
      MATCH(c:Comunicação) RETURN DISTINCT(c.nome) AS nome
    """
    try:
      result = tx.run(query)
      return [{
          'nome':row['nome']
      } for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise
    
def marriage_years(tx):
    query = """
      MATCH (p1:Pessoa {nome: 'Donizete'})-[r:CASADO_COM]->(p2:Pessoa {nome: 'Celia'}) RETURN r.anos AS anos
    """
    try:
      result = tx.run(query)
      record = result.single()
      return {'anos': record['anos']} if record else None
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def get_woman(tx):
    query = """
        MATCH (p:Pessoa) WHERE p.sexo = 'F' RETURN p.nome AS nome
    """
    try:
      result = tx.run(query)
      return [{
          'nome':row['nome']
      } for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def get_pets_and_owners(tx):
    query = """
        MATCH (p:Pessoa)-[:DONO_DE]->(c:Cachorro)
        RETURN c.nome AS cachorro, p.nome AS dono
    """
    try:
        result = tx.run(query)
        return [{
            'cachorro': row['cachorro'],
            'dono': row['dono']
        } for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise


def main():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "neo4jneo4j"

    driver = GraphDatabase.driver(uri, auth=(user, password))

    while True:
        print("\nMenu Interativo:")
        print("1 - Quem são os nomes das pessoas da família")
        print("2 - Quem são as mulheres da família")
        print("3 - Quem são os produtores rurais")
        print("4 - Quem trabalha no ramo de comunicação")
        print("5 - Há quantos anos Donizete e Celia são casados")
        print("6 - Quem é o pet da família e quem é seu dono?")
        print("7 - Sair")
        
        opcao = input("Escolha uma opção: ")

        with driver.session() as session:
            if opcao == "1":
                result = session.execute_read(get_family)
                if result:
                    print("\nNomes das pessoas da família:")
                    for person in result:
                        print(person['nome'])
                else:
                    print("\nNenhuma família encontrada.")
            
            elif opcao == "2":
                result = session.execute_read(get_woman)
                if result:
                    print("\nNomes das mulheres da família:")
                    for person in result:
                        print(person['nome'])
                else:
                    print("\nNenhuma mulher encontrada.")
            
            elif opcao == "3":
                result = session.execute_read(get_farmer)
                if result:
                    print("\nNomes dos produtores rurais:")
                    for person in result:
                        print(person['nome'])
                else:
                    print("\nNenhum produtor rural encontrado.")
            
            elif opcao == "4":
                result = session.execute_read(get_comunicators)
                if result:
                    print("\nNomes das pessoas que trabalham com comunicação:")
                    for person in result:
                        print(person['nome'])
                else:
                    print("\nNenhuma pessoa encontrada no ramo de comunicação.")
            
            elif opcao == "5":
                result = session.execute_read(marriage_years)
                if result:
                    print(f"\nCelia e Donizete são casados há {result['anos']} anos.")
                else:
                    print("\nNenhuma informação sobre o casamento foi encontrada.")
            
            elif opcao == "6":
                result = session.execute_read(get_pets_and_owners)
                if result:
                    print("\nLista de pets e seus donos:")
                    for pets in result:
                        print(f"{pets['cachorro']} é de {pets['dono']}")
                else:
                    print("\nNenhum cachorro com dono encontrado.")

            elif opcao == "7":
                print("\nSaindo do programa...")
                break
            
            else:
                print("\nOpção inválida. Tente novamente.")

    driver.close()

if __name__ == "__main__":
    main()