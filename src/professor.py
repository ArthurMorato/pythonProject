class Professor:
    def __init__(self, nome, disciplina, turma):
        self.nome = nome
        self.disciplina = disciplina
        self.turma = turma
        self.alunos = []  # inicializa uma lista vazia para armazenar os alunos do professor

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)  # adiciona o aluno à lista de alunos do professor

    def mostrar_informacoes(self):
        print(
            f"Professor: {self.nome}, Disciplina: {self.disciplina}, Turma: {self.turma}, Alunos: {[a.nome for a in self.alunos]}")