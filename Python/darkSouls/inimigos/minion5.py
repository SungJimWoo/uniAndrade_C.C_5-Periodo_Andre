from .minion import Minion

class FeiticeiroCorrompido(Minion):
    def __init__(self):
        super().__init__("Feiticeiro Corrompido", vida=140, dano=13, recompensa=35)