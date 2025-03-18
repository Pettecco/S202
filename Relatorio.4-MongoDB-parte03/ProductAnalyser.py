class ProductAnalyzer:
    def __init__(self, db):
      self.db = db

    def sellsPerDay(self):
      return self.db.collection.aggregate([
        {"$group": {
          "_id": "$data_compra", 
          "total_compras": {"$sum": 1} 
        }},
      ])

    def mostSelledProduct(self):
      return self.db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group" : {
          "_id": "$produtos.descricao",
          "total": {"$sum": "$produtos.quantidade"},
        }},
          {"$sort": {"quantidade_total": -1}},
          {"$limit": 1}
      ])

    def clientWhoSpentMost(self):
      return self.db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$addFields": {
          "total_gasto_produto": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}
        }},
        {"$group": {
          "_id": "$_id",
          "cliente_id": {"$first": "$cliente_id"},
          "total_gasto": {"$sum": "$total_gasto_produto"}
        }},
        {"$sort": {"total_gasto": -1}},
        {"$limit": 1}
      ])   

    def productsWithMoreThanOneSold(self):
      return self.db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {
          "_id": "$produtos.descricao",
          "quantidadeVendida": {"$sum": "$produtos.quantidade"}
        }},
        {"$match": {
          "quantidadeVendida": {"$gt": 1} 
        }}
      ])
