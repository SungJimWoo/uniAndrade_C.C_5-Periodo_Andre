from jogadores.jogador import Jogador

class Cavaleiro(Jogador):
    def __init__(self, nome: str, dano: int = 20, armadura: str = "Escudo", resistencia: int = 85):
        super().__init__(nome, dano)
        self.armadura = armadura
        self.resistencia = resistencia

    def atacar(self, inimigo):
        print(f"{self.nome} desfere um golpe poderoso!")
        inimigo.defender(self.dano)

    def defender(self, dano: int, inimigo=None):
        reducao = getattr(self, 'reducao_dano', 0)
        resistencia_extra = self.resistencia // 10
        dano_reduzido = max(dano - reducao - resistencia_extra, 0)
        dano_defendido = dano_reduzido // 2  # Reduz pela metade ao defender

        self.saude -= dano_defendido
        print(f"{self.nome} bloqueia com {self.armadura}! Sofre {dano_defendido}. Vida: {self.saude}")

        
