from minion import Minion

class ZumbiLento(Minion):
    def __init__(self):
        super().__init__("Zumbi Lento", vida=120, dano=10, recompensa=15)