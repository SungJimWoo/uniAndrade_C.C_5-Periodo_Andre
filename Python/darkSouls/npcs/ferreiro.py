from itens.arma import armas_disponiveis
from itens.armadura import armaduras_disponiveis

class Ferreiro:
    def __init__(self):
        self.inventario = armas_disponiveis + armaduras_disponiveis

    def listar_itens(self):
        print("\n--- Armas disponíveis ---")
        for i, item in enumerate(self.inventario, 1):
            if item.tipo == "arma":
                print(f"{i}. {item.nome} – Dano: {item.dano} – {item.preco}G")

        print("\n--- Armaduras disponíveis ---")
        for i, item in enumerate(self.inventario, 1):
            if item.tipo == "armadura":
                print(f"{i}. {item.nome} – Defesa: {item.defesa_extra} – {item.preco}G")

    def vender(self, jogador, escolha: int):
        if 1 <= escolha <= len(self.inventario):
            item = self.inventario[escolha - 1]
            if jogador.dinheiro >= item.preco:
                jogador.dinheiro -= item.preco
                jogador.inventario.append(item)
                print(f"{item.nome} foi adicionado ao seu inventário.")
            else:
                falta = item.preco - jogador.dinheiro
                print(f"\nVocê não tem ouro suficiente. Faltam {falta}G.")
                input("Pressione Enter para continuar...")
        else:
            print("Escolha inválida.")
            input("Pressione Enter para continuar...")