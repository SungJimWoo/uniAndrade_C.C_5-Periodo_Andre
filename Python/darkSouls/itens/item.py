from jogadores import jogador
class Item:
    def __init__(self, nome: str, tipo: str, preco: int):
        self.nome = nome
        self.tipo = tipo  # "arma", "armadura", "pocao"
        self.preco = preco

    def usar(self, jogador):
        pass  # será sobrescrito pelas subclasses