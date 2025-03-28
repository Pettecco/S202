from database import Database
from bookModel import BookModel
from cli import LibraryCLI

db = Database(database="relatorio_05", collection="livros")
db.resetDatabase()
bookModel = BookModel(database=db)

libraryCLI = LibraryCLI(bookModel)
libraryCLI.run()
