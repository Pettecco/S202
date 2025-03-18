from database import Database
from helper.writeAJson import writeAJson
from ProductAnalyser import ProductAnalyzer

db = Database(database="mercado", collection="compras")
db.resetDatabase()

productAnalyzer = ProductAnalyzer(db=db)

result = productAnalyzer.sellsPerDay()
writeAJson(result, "Total de vendas por dia")

result = productAnalyzer.mostSelledProduct()
writeAJson(result, "Produto mais vendido")

result = productAnalyzer.clientWhoSpentMost()
writeAJson(result, "Clinte que mais gastou")

result = productAnalyzer.productsWithMoreThanOneSold()
writeAJson(result, "Produtos com mais de uma unidade vendida")