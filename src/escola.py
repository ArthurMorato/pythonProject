class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []  # inicializa uma lista vazia para armazenar as disciplinas da escola

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)  # adiciona a disciplina à lista de disciplinas da escola

    def mostrar_informacoes(self):
        print(f"Escola: {self.nome}")
        for disciplina in self.disciplinas:
            disciplina.mostrar_informacoes()