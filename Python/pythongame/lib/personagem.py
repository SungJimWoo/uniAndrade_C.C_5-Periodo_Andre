# lib/personagem.py

class PersonagemGame:
    def __init__(self, nome, nivel, vida, classe):
        self.nome = nome
        self.nivel = nivel
        self.vida = vida
        self.classe = classe
        self.inventario = []  # opcional: estrutura de dados

    def atacar(self, inimigo):
        print(f"{self.nome} ataca {inimigo} com poder de nível {self.nivel}!")

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"{item} foi adicionado ao inventário de {self.nome}.")