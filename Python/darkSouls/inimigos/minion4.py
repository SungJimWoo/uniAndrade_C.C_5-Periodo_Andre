from minion import Minion

class EspiritoFlamejante(Minion):
    def __init__(self):
        super().__init__("Espírito Flamejante", vida=100, dano=16, recompensa=30)