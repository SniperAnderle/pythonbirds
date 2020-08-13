"""
Criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:
1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
A) Atributo de dado velocidade
B) Método acelerar, que deverá incrementar a velocidade de uma unidade
C) Método frear que deverá diminuir a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:
A) Valor de direção com possíveis: Norte, Sul, Leste, Oeste
B) Método girar_a_direita
C) Método girar_a_esquerda
  N
O   L
  S

    Exemplo:
    >>># Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>># Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
        >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
        >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> direcao.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> direcao.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> direcao.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Oeste'
"""


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'
class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]



class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        # self.velocidade -= 2
        # self.velocidade = max(0, self.velocidade)
        if self.velocidade == 1:
            self.velocidade -= 1
        elif self.velocidade == 0:
            self.velocidade = 0
        else:
            self.velocidade -= 2
