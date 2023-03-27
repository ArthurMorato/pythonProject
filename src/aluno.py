class Aluno:
    def __init__(self, nome, idade, serie):
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.notas = []  # inicializa uma lista vazia para armazenar as notas do aluno

    def adicionar_nota(self, nota):
        self.notas.append(nota)  # adiciona a nota do aluno à lista de notas

    def mostrar_informacoes(self):
        print(f"Aluno: {self.nome}, Idade: {self.idade}, Série: {self.serie}, Notas: {self.notas}")