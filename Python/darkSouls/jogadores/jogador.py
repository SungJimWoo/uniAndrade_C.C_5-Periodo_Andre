from abc import ABC, abstractmethod
class jogador:
    def __init__(self, nome:str, dano:int):
        self.nome = nome
        self.dano = dano
        self.__saude = 100 #encapsulamento

        @property # Encapsulamento com property
        def saude(self) -> int:
            return self.__saude

        @saude.setter 
        def saude(self, valor: int):
            # Garante que a vida nunca seja negativa
            self.__saude = max(0, valor)

        @abstractmethod # Métodos que as subclasses DEVEM sobrescrever
        def atacar(self, inimigo): 
            print(f"{self.nome} atacou {inimigo.nome}!")

        @abstractmethod # Obriga as classes filhas a implementarem
        def defender(self):
            self.saude -= dano
            print(f"{self.nome} defendeu o ataque! Vida agora: {self.saude}")

        def esta_vivo(self) -> bool:
            # Retorna True se a saúde for maior que zero.
            return self.saude > 0