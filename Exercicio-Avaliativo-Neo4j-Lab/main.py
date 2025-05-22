from database import Database
from TeacherCRUD import TeacherCRUD
from cli import TeacherCLI
from query import TeacherDatabase

db = Database("bolt://localhost:7687", "neo4j", "neo4jneo4j")

teacherDB = TeacherDatabase(db)
teacherCRUD = TeacherCRUD(db)
teacherCLI = TeacherCLI(teacherCRUD)

print("\nQuestão 1:")
teacherDB.professor_name()
teacherDB.professor_first_letter()
teacherDB.city()
teacherDB.school()

print("\nQuestão 2:")
teacherDB.professor_age()
teacherDB.avg_population()
teacherDB.cep_city()
teacherDB.third_letter()

print("\nQuestão 3:")
teacherCRUD.create('Chris Lima', 1956, '189.052.396-66')
chris = teacherCRUD.read("Chris Lima")
print(f"Ano de Nascimento: {chris[0][0]}\nCPF: {chris[0][1]}")
teacherCRUD.update("Chris Lima", "162.052.777-77")
chris = teacherCRUD.read("Chris Lima")
print(f"Ano de Nascimento: {chris[0][0]}\nCPF: {chris[0][1]}")
teacherCLI.run()


db.close()