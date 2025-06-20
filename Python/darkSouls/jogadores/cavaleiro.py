from jogadores.jogador import jogador
class Cavaleiro(jogador): # Herança
    def __init__(self, nome:str, dano:int, armadura="Diamante", resistencia=85):
        super().__init__(nome, dano)
        self.armadura = armadura #encapsulamento
        self.resistencia = resistencia # atributos extras
        super().__init__(nome, dano)

    @property # Decorador retorna apenas com propriedade
    def saude(self):
        return self.__saude

    @saude.setter # Decorador retorna apenas com propriedade
    def saude(self, valor):
        self.saude += max(0, valor)

    def atacar(self):
        print("Atacar Polimorfico") 
        print(f"{self.nome} atacou!")

    def defender(self):
        print("Defender Polimorfico")
        print(f"{self.nome} defendeu!")

if __name__ == "__main__":
    cavaleiro = Cavaleiro("rei Arthur", 80)
    cavaleiro.atacar()