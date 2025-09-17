
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        def apresentar(self):
            return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos'
        
class Atleta(Pessoa):
    def __init__(self, nome, idade, modalidade):
        super().__init__(nome, idade)
        self.modalidade = modalidade

        # sobreescrever apresentar()
    def apresentar(self):
        info = super().apresentar()
        print(f'{info}, eu sou atleta de {self.modalidade}')


class Equipe:
    def __init__(self, nome_equipe):
        self.nome_equipe = nome_equipe
        self.lista_atletas = []

    def adicionar_atleta(self, atleta):
        self.lista_atletas.append(atleta)
        return f'Atleta {atleta} adicionado'
    
    def listar_atletas(self):
        for atleta in self.lista_atletas:
            print(atleta)

    def contar_atletas(self):
        return f'Esta equipe tem um total de {len(self.lista_atletas)} atletas'

atleta1 = Atleta('julia', 18, 'corredora')
atleta2 = Atleta('Roberto', 15, 'corredor')
atleta3 = Atleta('Nanny', 28, 'jogadora de MU')

equipe1 = Equipe('equipe_corredores')

print(equipe1.adicionar_atleta(atleta1.nome))
print(equipe1.adicionar_atleta(atleta2.nome))
print(equipe1.adicionar_atleta(atleta3.nome))

print()
equipe1.listar_atletas()
print()
print(equipe1.contar_atletas())