from .item import Item
import time

class Pocao(Item):
    def __init__(self, nome: str, efeito: str, valor: int, preco: int):
        super().__init__(nome, tipo="pocao", preco=preco)
        self.efeito = efeito  # "cura" ou "buff"
        self.valor = valor

    def usar(self, jogador):
        if self.efeito == "cura":
            jogador.saude = min(jogador.saude + self.valor, jogador.vida_maxima)
            print(f"{jogador.nome} usou {self.nome} e recuperou {self.valor} de vida!")
        elif self.efeito == "buff":
            print(f"{jogador.nome} bebe {self.nome}... preparando buff...")
            time.sleep(1)  # entrega o turno
            jogador.dano += self.valor
            print(f"{jogador.nome} recebeu um BUFF! Dano aumentado em {self.valor}.")

# Lista de poções disponíveis
pocoes_disponiveis = [
    Pocao("Poção Fraca", "cura", 20, 10),
    Pocao("Poção Média", "cura", 50, 25),
    Pocao("Poção Forte", "cura", 100, 50),
    Pocao("Poção de Força", "buff", 10, 20)
]