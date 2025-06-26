class Estalagem:
    def __init__(self, preco=30):
        self.preco = preco

    def descansar(self, jogador):
        if jogador.dinheiro >= self.preco:
            jogador.dinheiro -= self.preco
            jogador.saude = jogador.vida_maxima
            print(f"\n{jogador.nome} descansou e recuperou toda a vida!") 
            input("Pressione Enter para continuar...")
        else:
            print("\nVocê não tem ouro suficiente para descansar.")
            input("Pressione Enter para continuar...")