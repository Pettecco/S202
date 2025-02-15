class Professor:
  def __init__(self, nome):
    self.nome = nome
  
  def ministrar_aula(self, assunto):
    print(f'O professor {self.nome} está ministrando uma aula sobre {assunto}')

class Aluno:
  def __init__(self, nome):
    self.nome = nome
  
  def presenca(self):
    print(f'O aluno {self.nome} está presente')

class Aula:
  def __init__(self, professor, assunto):
    self.professor = professor
    self.assunto = assunto
    self.alunos = []
  
  def adiciona_aluno(self, aluno):
    self.alunos.append(aluno)
  
  def listar_presenca(self):
    print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
    for i in self.alunos:
      print(i.nome)
  
jonas = Professor('Jonas')
jonas.ministrar_aula('banco de dados 2')

petterson = Aluno('Petterson')
petterson.presenca()

joao = Aluno('João')
maria = Aluno('Maria')
gabriel = Aluno('Gabriel')

aula = Aula(jonas, 'Banco de Dados II')
aula.adiciona_aluno(petterson)
aula.adiciona_aluno(joao)
aula.adiciona_aluno(maria)
aula.adiciona_aluno(gabriel)

aula.listar_presenca()