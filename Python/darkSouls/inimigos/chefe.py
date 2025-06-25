class Chefe:
    def __init__(self, nome, vida, dano, recompensa):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.recompensa = recompensa  # ouro, item, etc.

    def atacar(self, jogador):
        print(f"{self.nome} ataca com força! Causa {self.dano} de dano.")
        jogador.receber_dano(self.dano)

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0