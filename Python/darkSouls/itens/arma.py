from .item import Item

class Arma(Item):
    def __init__(self, nome: str, dano: int, preco: int):
        super().__init__(nome, tipo="arma", preco=preco)
        self.dano = dano

    def usar(self, jogador):
        jogador.dano += self.dano
        jogador.arma_atual = self.nome
        print(f"{jogador.nome} equipou {self.nome}! Dano aumentado em {self.dano}.")

# Lista de armas disponíveis
armas_disponiveis = [
    Arma("Espada de Ferro", 30, 50),
    Arma("Lança Rúnica", 45, 80),
    Arma("Machado Pesado", 60, 100),
    Arma("Espada do Abismo", 100, 325)  # NOVA arma poderosa, preço alto!
]