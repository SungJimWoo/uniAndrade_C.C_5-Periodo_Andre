from .minion import Minion

class CapraDemon(Minion):
    def __init__(self):
        super().__init__("Capra Demon", vida=1176, dano=30, recompensa=150)