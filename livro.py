class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.avaliacoes = []

    def avaliar(self, nota):
        self.avaliacoes.append(nota)

    def media_avaliacoes(self):
        if self.avaliacoes:
            return sum(self.avaliacoes) / len(self.avaliacoes)
        return 0