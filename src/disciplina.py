class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []  # inicializa uma lista vazia para armazenar os professores da disciplina

    def adicionar_professor(self, professor):
        self.professores.append(professor)  # adiciona o professor à lista de professores da disciplina

    def mostrar_informacoes(self):
        print(f"Disciplina: {self.nome}, Professores: {[p.nome for p in self.professores]}")