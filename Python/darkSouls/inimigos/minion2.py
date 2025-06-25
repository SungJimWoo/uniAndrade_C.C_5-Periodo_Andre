from .minion import Minion

class VampiroFraco(Minion):
    def __init__(self):
        super().__init__("Vampiro Fraco", vida=130, dano=12, recompensa=20)