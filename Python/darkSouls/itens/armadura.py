from .item import Item

class Armadura(Item):
    def __init__(self, nome: str, defesa_extra: int, preco: int):
        super().__init__(nome, tipo="armadura", preco=preco)
        self.defesa_extra = defesa_extra

    def usar(self, jogador):
        jogador.resistencia += self.defesa_extra
        jogador.armadura_atual = self.nome
        print(f"{jogador.nome} equipou {self.nome}! Resistência +{self.defesa_extra}.")

# Lista de armaduras disponíveis
armaduras_disponiveis = [
    Armadura("Cota de Couro", 5, 20),
    Armadura("Armadura de Aço", 10, 40),
    Armadura("Armadura Real", 15, 60)
]