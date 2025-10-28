class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []
        self.avaliacao_atendimento = None

    def emprestar_livro(self, livro):
        if livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.disponivel = False
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
            return True
        return False

    def avaliar_livro(self, livro, nota):
        livro.avaliar(nota)

    def avaliar_atendimento(self, nota):
        self.avaliacao_atendimento = nota