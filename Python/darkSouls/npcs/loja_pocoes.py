from itens.pocao import pocoes_disponiveis, Pocao

class Loja:
    def listar_pocoes(self):
        print("\n--- Loja de Poções ---")
        for i, pocao in enumerate(pocoes_disponiveis, 1):
            if pocao.efeito == "cura":
                print(f"{i}. {pocao.nome} ({pocao.efeito}) - Cura: {pocao.valor} - Preço: {pocao.preco}")
            elif pocao.efeito == "buff":
                print(f"{i}. {pocao.nome} ({pocao.efeito}) - Bônus: +{pocao.valor} dano - Preço: {pocao.preco}")
            else:
                print(f"{i}. {pocao.nome} ({pocao.efeito}) - Valor: {pocao.valor} - Preço: {pocao.preco}")

    def vender_pocao(self, jogador, escolha: int):
        if 1 <= escolha <= len(pocoes_disponiveis):
            base = pocoes_disponiveis[escolha - 1]
            nova_pocao = Pocao(base.nome, base.efeito, base.valor, base.preco)

            if jogador.dinheiro >= nova_pocao.preco:
                jogador.dinheiro -= nova_pocao.preco
                jogador.inventario.append(nova_pocao)
                print(f"{nova_pocao.nome} foi adicionada ao seu inventário.")
            else:
                print("\nVocê não tem ouro suficiente.")
                input("Pressione Enter para continuar...")
        else:
            print("\nEscolha inválida.")
            input("Pressione Enter para continuar...")
