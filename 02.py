

class Planta:
    def __init__(self, especie):
        self.especie = especie

class Cacto(Planta):
    def __init__(self, especie):
        super().__init__(especie)

cacto1 = Cacto('Opuntia')
print(cacto1.especie)