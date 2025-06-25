from .item import Item

class Arma(Item):
    def __init__(self, nome: str, dano_extra: int, preco: int):
        super().__init__(nome, tipo="arma", preco=preco)
        self.dano_extra = dano_extra

    def usar(self, jogador):
        jogador.dano += self.dano_extra
        jogador.arma_atual = self.nome
        print(f"{jogador.nome} equipou {self.nome}! Dano aumentado em {self.dano_extra}.")

# Lista de armas disponíveis
armas_disponiveis = [
    Arma("Espada de Ferro", 10, 25),
    Arma("Lança Rúnica", 15, 40),
    Arma("Machado Pesado", 20, 60),
    Arma("Espada do Abismo", 50, 250)  # NOVA arma poderosa, preço alto!
]