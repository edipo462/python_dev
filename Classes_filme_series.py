class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property #O property é utilizado para retornar o atributo privado de uma classe
    def nome (self):
        return self._nome

    @nome.setter #serve para alterar o valor de um atributo privado de uma classe

    def nome (self, novo_filme):
        self._nome = novo_filme.title()


    def dar_like (self):
        self._like += 1



    @property
    def like (self):
        return self._like

    def __str__(self):
        return "Filme: {}, Ano: {}, Duração: {}, Likes: {}".format(self.nome, self.like)


#criando uma classe Filme com herança da classe principal (Programa)

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "Filme: {}, Ano: {}, Duração: {}, Likes: {}".format(self.nome, self.ano, self.duracao, self.like)

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
#str é uma maneira de retornar uma string de um metodo
    def __str__(self):
        return "Filme: {}, Ano: {}, Temporadas: {}, Likes: {}".format(self.nome, self.ano, self.temporadas, self.like)

class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property

    def listagem (self):
        return self._programas

    @property

    def tamanho (self):
        return len(self._programas)