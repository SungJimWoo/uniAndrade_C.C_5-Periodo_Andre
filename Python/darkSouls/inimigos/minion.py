class Minion:
    def __init__(self, nome, vida, dano, recompensa):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.recompensa = recompensa

    def atacar(self, jogador):
        jogador.saude -= self.dano
        print(f"{self.nome} ataca {jogador.nome}, causando {self.dano} de dano!")

    def defender(self, dano_recebido):
        self.vida -= dano_recebido
        print(f"{self.nome} recebeu {dano_recebido} de dano. Vida restante: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0