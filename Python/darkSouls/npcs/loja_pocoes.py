from itens.pocao import pocoes_disponiveis

class Loja:
    def listar_pocoes(self):
        print("\n--- Loja de Poções ---")
        for i, pocao in enumerate(pocoes_disponiveis, 1):
            print(f"{i}. {pocao.nome} ({pocao.efeito}) - Valor: {pocao.valor} - Preço: {pocao.preco}")

    def vender_pocao(self, jogador, escolha: int):
        if 1 <= escolha <= len(pocoes_disponiveis):
            pocao = pocoes_disponiveis[escolha-1]
            if jogador.dinheiro >= pocao.preco:
                jogador.dinheiro -= pocao.preco
                jogador.inventario.append(pocao)
                print(f"{pocao.nome} foi adicionada ao seu inventário.")
            else:
                print("Você não tem ouro suficiente.")
        else:
            print("Escolha inválida.")