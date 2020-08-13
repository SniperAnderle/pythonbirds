class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    sarah = Pessoa(nome='Sarah')
    patricia = Pessoa(sarah, nome='Patrícia')
    print(Pessoa.cumprimentar(patricia))
    print(id(patricia))
    print(patricia.cumprimentar())
    print(patricia.nome)
    print(patricia.idade)
    for filho in patricia.filhos:
        print(filho.nome)
