class Programa: #A classe programa foi criada pois nas subClasses existem vamos usar atributos semelhantes

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

#O property é utilizado para retornar o atributo privado de uma classe
    @property 
    def nome (self):
        return self._nome

#o "setter" serve para alterar um atributo de forma segura, principalmente se esse atributo for privado
# 
    @nome.setter 
    def nome (self, novo_filme):
        self._nome = novo_filme.title()


    def dar_like (self):
        self._like += 1


    @property
    def like (self):
        return self._like

#Classe criada para o objeto Filme, utilizando a herança da Classe "Programa"
class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def retorna_playlist (self):
        return print ("Filme: {}, Ano: {}, Duração: {}, Likes: {}".format(self.nome, self.ano, self.duracao, self.like))

#Classe criada para o objeto Serie, utilizando a herança da Classe "Programa"
class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def retorna_playlist (self):
        return print ("Filme: {}, Ano: {}, Duração: {}, Likes: {}".format(self.nome, self.ano, self.temporadas, self.like))    
