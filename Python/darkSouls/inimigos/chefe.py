from .minion import Minion

class SenhorDasCinzas(Minion):
    def __init__(self):
        super().__init__("Senhor das Cinzas", vida=180, dano=25, recompensa=100)