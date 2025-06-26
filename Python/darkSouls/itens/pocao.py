from .item import Item
import time

class Pocao(Item):
    def __init__(self, nome: str, efeito: str, valor: int, preco: int, quantidade: int = 1):
        super().__init__(nome, tipo="poção", preco=preco)
        self.efeito = efeito  # "cura" ou "buff"
        self.valor = valor
        self.quantidade = quantidade

    def usar(self, jogador):
        if self.efeito == "cura":
            jogador.saude = min(jogador.saude + self.valor, jogador.vida_maxima)
            print(f"{jogador.nome} usou {self.nome} e recuperou {self.valor} de vida!")
        elif self.efeito == "buff":
            print(f"{jogador.nome} bebe {self.nome}... preparando buff...")
            time.sleep(1)
            jogador.dano += self.valor
            print(f"{jogador.nome} recebeu um BUFF! Dano aumentado em {self.valor}.")
        self.quantidade -= 1

# Lista base de poções (modelos)
pocoes_disponiveis = [
    Pocao("Poção Fraca", "cura", 20, 10),
    Pocao("Poção Média", "cura", 50, 25),
    Pocao("Poção Forte", "cura", 100, 50),
    Pocao("Poção de Força", "buff", 10, 20)
]
