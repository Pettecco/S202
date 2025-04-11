from MotoristaDAO import MotoristaDAO
from database import Database
from MotoristaCLI import MotoristaCLI

db = Database(database="Motoristas", collection="Motoristas")
motorista_DAO = MotoristaDAO(db)

MotoristaCLI = MotoristaCLI(motorista_DAO)
MotoristaCLI.run()