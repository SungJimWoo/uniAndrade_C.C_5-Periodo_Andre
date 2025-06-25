from .minion import Minion

class LoboSombrio(Minion):
    def __init__(self):
        super().__init__("Lobo Sombrio", vida=110, dano=14, recompensa=25)