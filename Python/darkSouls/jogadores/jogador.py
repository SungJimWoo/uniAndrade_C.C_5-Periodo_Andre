from abc import ABC, abstractmethod

class Jogador(ABC): # Herança
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano
        self.__saude = 100 # Encapsulamento

    @property # Decorador retorna apenas como propriedade
    def saude(self):
        return self.__saude

    @saude.setter # Decorador retorna apenas como propriedade
    def saude(self, valor):
        self.__saude = max(0, valor)

    @abstractmethod # Obriga as classes filhas a implementarem
    def atacar(self):
        print(f"{self.nome} atacou!")

    @abstractmethod # Obriga as classes filhas a implementarem
    def defender(self):
        print(f"{self.nome} defendeu!")

