class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}.'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe} Aperto de mão.'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    sarah = Mutante(nome='Sarah')
    patricia = Mulher(sarah, nome='Patrícia')
    print(Pessoa.cumprimentar(patricia))
    print(id(patricia))
    print(patricia.cumprimentar())
    print(patricia.nome)
    print(patricia.idade)
    for filho in patricia.filhos:
        print(filho.nome)
    patricia.sobrenome = 'de Souza Costa'
    del patricia.filhos
    patricia.olhos = 1
    del patricia.olhos
    print(patricia.__dict__)
    print(sarah.__dict__)
    print(Pessoa.olhos)
    print(patricia.olhos)
    print(sarah.olhos)
    print(id(Pessoa.olhos), id(patricia.olhos), id(sarah.olhos))
    print(Pessoa.metodo_estatico(), patricia.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), patricia.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Mulher))
    print(isinstance(sarah, Pessoa))
    print(isinstance(sarah, Mulher))
    print(sarah.olhos)
    print(patricia.cumprimentar())
    print(sarah.cumprimentar())