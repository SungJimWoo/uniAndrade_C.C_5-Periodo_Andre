from jogadores.jogador import jogador

class Cavaleiro(jogador):
    def __init__(self, nome: str, dano: int = 20, armadura: str = "Diamante", resistencia: int = 85):
        super().__init__(nome, dano)
        self.armadura = armadura
        self.resistencia = resistencia

    # sobrescrevendo métodos abstratos
    def atacar(self, inimigo):
        print(f"{self.nome} desfere um golpe poderoso!")
        inimigo.defender(self.dano)

    def defender(self, dano: int):
        dano_recebido = max(0, dano - self.resistencia // 10)
        self.saude = self.saude - dano_recebido
        print(f"{self.nome} bloqueia com {self.armadura}! Sofre {dano_recebido}. Vida: {self.saude}")