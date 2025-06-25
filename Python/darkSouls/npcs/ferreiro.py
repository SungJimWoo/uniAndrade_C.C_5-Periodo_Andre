from itens import item

class Ferreiro:
    def __init__(self):
        self.inventario = armas_disponiveis + armaduras_disponiveis

    def listar_itens(self):
        print("\n--- Itens disponíveis no ferreiro ---")
        for i, item in enumerate(self.inventario, 1):
            print(f"{i}. {item.nome} ({item.tipo}) - Preço: {item.preco}")

    def vender(self, jogador, escolha: int):
        if 1 <= escolha <= len(self.inventario):
            item = self.inventario[escolha - 1]
            if jogador.dinheiro >= item.preco:
                jogador.dinheiro -= item.preco
                jogador.inventario.append(item)
                print(f"{item.nome} foi adicionado ao seu inventário.")
            else:
                print("Você não tem ouro suficiente.")
        else:
            print("Escolha inválida.")