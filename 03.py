class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self,nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso


aluno1 = Estudante("João", 26, "Programação")
print(aluno1.__dict__)