class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 10
        self.vivo = True

    def usar_pocao(self, pocao):
        self.saude += pocao.potencia
        print(f"Personagem {self.nome} usou poção de {pocao.tipo}")
        if pocao1:
            print(f"Cura {pocao.potencia} saúde {self.saude}")
        elif pocao2:
            print(f"Veneno {pocao.potencia} saúde {self.saude}")

class PocaoVerde:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class PocaoRoxa:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

#Crie uma nova PocaoRoxa

#Instanciar Jogador
p1 = Personagem("Chaves")
pocao1 = PocaoVerde("Cura", 15)
pocao2 = PocaoRoxa("Veneno", 5)
p1.usar_pocao(pocao2),



# Se o personagem ainda está vivo, decremente ao usar a poção veneno
    # Pode usar poção veneno
    # Pode usar poção saúde
# Se a saúde for <= 0
    # Personagem vivo = False
    # Informe personagem está morto, foi de "arrasta"
    # Cancele a possibilidade de incrementar ou decrementar saúde