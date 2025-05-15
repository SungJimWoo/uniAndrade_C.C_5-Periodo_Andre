class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 10
        self.vivo = True

    def usar_pocao(self, pocao):
        if not self.vivo:
            print(f"{self.nome} está morto e não pode usar poções.")
            return

        if pocao.tipo == "Cura":
            if self.saude == 10:
                print(f"{self.nome} já está com a vida cheia")
            else:
                self.saude -= pocao.potencia
                if self.saude > 10:
                    self.saude = 10  # Limita a saúde máxima
                    print(f"{self.nome} usou poção de cura: +{pocao.potencia} de saúde. Saúde atual: {self.saude}")

        elif pocao.tipo == "Dano":
            self.saude -= pocao.potencia
            print(f"{self.nome} usou poção de veneno: -{pocao.potencia} de saúde. Saúde atual: {self.saude}")

        if self.saude <= 0:
            self.vivo = False
            print(f"{self.nome} foi de arrasta!")
            

class PocaoVerde:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class PocaoRoxa:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

# Criando personagem e poções
p1 = Personagem("Chaves")
pocao1 = PocaoVerde("Cura", 15)
pocao2 = PocaoRoxa("Dano", 12)

# Teste de uso das poções
p1.usar_pocao(pocao1)  # Aplica dano
p1.usar_pocao(pocao2)  # Se ainda estiver vivo, aplica cura

# Se o personagem ainda está vivo, decremente ao usar a poção veneno
    # Pode usar poção veneno
    # Pode usar poção saúde
# Se a saúde for <= 0
    # Personagem vivo = False
    # Informe personagem está morto, foi de "arrasta"
    # Cancele a possibilidade de incrementar ou decrementar saúde