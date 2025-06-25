from abc import ABC, abstractmethod

class Jogador(ABC):
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano
        self.__saude = 100  # Atributo privado com encapsulamento
        self.inventario = []  # Inicialização aqui já evita erro
        self.dinheiro = 0     # Para compras e recompensas
        self.vida_maxima = 100 

    @property
    def saude(self) -> int:
        return self.__saude

    @saude.setter
    def saude(self, valor: int):
        self.__saude = max(0, valor)  # Nunca abaixo de zero

    @abstractmethod
    def atacar(self, inimigo):
        pass

    @abstractmethod
    def defender(self, dano: int):
        pass

    def esta_vivo(self) -> bool:
        return self.saude > 0