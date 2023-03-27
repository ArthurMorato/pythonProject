from src.aluno import Aluno
from src.disciplina import Disciplina
from src.escola import Escola
from src.professor import Professor

def main():
    # Criar alunos
    aluno1 = Aluno("Migewrewl Pererewrewrira", 63, 14)
    aluno2 = Aluno("Marrewia Evelrewryn", 226, 133)
    aluno1.adicionar_nota(8.5)
    aluno1.adicionar_nota(7.0)
    aluno2.adicionar_nota(9.0)
    aluno2.adicionar_nota(7.5)

    # Criar professores e turmas
    professor1 = Professor("Bozo", "Bagunça", 922222)
    professor2 = Professor("Aleatória", "Português", 9333333333)
    professor1.adicionar_aluno(aluno1)
    professor1.adicionar_aluno(aluno2)
    professor2.adicionar_aluno(aluno1)
    professor2.adicionar_aluno(aluno2)

    # Criar disciplinas e adicioná-las aos professores
    matematica = Disciplina("Metidsadasdasdmeti")
    portugues = Disciplina("Pfasdafasdfgasortugal")
    matematica.adicionar_professor(professor1)
    portugues.adicionar_professor(professor2)

    # Criar escola e adicionar disciplinas
    escola = Escola("Escogadasfla da Bagunasfgdsfgasdfgwtwça")
    escola.adicionar_disciplina(matematica)
    escola.adicionar_disciplina(portugues)

    # Mostrar informações
    escola.mostrar_informacoes()
    matematica.mostrar_informacoes()
    portugues.mostrar_informacoes()
    professor1.mostrar_informacoes()
    professor2.mostrar_informacoes()
    aluno1.mostrar_informacoes()
    aluno2.mostrar_informacoes()



if __name__ == '__main__':
    main()

