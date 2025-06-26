import random
import os

from jogadores.cavaleiro import Cavaleiro
from inimigos import ZumbiLento, VampiroFraco, LoboSombrio, EspiritoFlamejante, FeiticeiroCorrompido, CapraDemon
from npcs.loja_pocoes import Loja
from npcs.ferreiro import Ferreiro
from npcs.estalagem import Estalagem
from itens.pocao import pocoes_disponiveis

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def barra_vida(atual, maximo, tamanho=30):
    proporcao = atual / maximo
    cheio = int(tamanho * proporcao)
    vazio = tamanho - cheio
    barra = "█" * cheio + " " * vazio
    return f"[{barra}] {atual}/{maximo}"

def mostrar_menu_principal(jogador):
    limpar_tela()
    print("\n" + "-"*60)
    print(f"Vida : {barra_vida(jogador.saude, 100)}")
    print(f"Esp  : {barra_vida(0, 100)}")
    print(f"Gold : {jogador.dinheiro} G")
    print("-"*60)
    print("1. Iniciar batalha")
    print("2. Loja de poções")
    print("3. Ferreiro (itens)")
    print("4. Estalagem (curar 30G)")
    print("5. Inventário")
    print("6. Sair")
    return input("Escolha: ")

def consultar_inv(inv, cav=None):
    limpar_tela()
    print("\n--- INVENTÁRIO ---")
    if not inv:
        print("Vazio.")
    else:
        for i, item in enumerate(inv, 1):
            tipo = getattr(item, 'tipo', '')
            if tipo == "poção":
                print(f"{i}. {item.nome} (+{item.valor}) – qtd {item.quantidade}")
            elif tipo == "arma":
                print(f"{i}. {item.nome} (arma) – dano {item.dano}")
            elif tipo == "armadura":
                print(f"{i}. {item.nome} (armadura) – defesa +{item.defesa_extra}")

    if cav is None:
        input("Enter para voltar…")
        return

    print("\n--- EQUIPADO ---")
    print(f"Arma equipada    : {getattr(cav, 'arma_nome', 'Nenhuma')}")
    print(f"Armadura equipada: {getattr(cav, 'armadura_nome', 'Nenhuma')}")

    esc = input("\nNº do item para usar/equipar ou Enter para voltar: ")
    if not esc.isdigit():
        return
    idx = int(esc) - 1
    if 0 <= idx < len(inv):
        item = inv[idx]
        tipo = getattr(item, 'tipo', '')
        if tipo == "poção":
            item.usar(cav)
            if item.quantidade <= 0:
                inv.pop(idx)
        elif tipo == "arma":
            cav.dano = item.dano
            cav.arma_nome = item.nome
            print(f"{item.nome} equipada! Dano agora: {cav.dano}")
        elif tipo == "armadura":
            cav.reducao_dano = item.defesa_extra
            cav.armadura_nome = item.nome
            print(f"{item.nome} equipada! Redução de dano: {cav.reducao_dano}%")
    else:
        print("Opção inválida.")

def escolher_inimigo():
    limpar_tela()
    print("\n--- ESCOLHA SEU DESAFIO ---")
    print("1. Chefe: Capra Demon")
    print("2. Peregrinos Perdidos (aleatório)")
    escolha = input("Número do inimigo: ")
    if escolha == "1":
        return CapraDemon()
    else:
        return random.choice([
            ZumbiLento(),
            VampiroFraco(),
            LoboSombrio(),
            EspiritoFlamejante(),
            FeiticeiroCorrompido()
        ])

def batalha(jogador, inimigo):
    print(f"\nInimigo: {inimigo.nome} apareceu!")
    while jogador.esta_vivo() and inimigo.esta_vivo():
        print("\n" + "-"*60)
        print(f"{inimigo.nome}: {barra_vida(inimigo.vida, inimigo.vida)}")
        print(f"{jogador.nome} : {barra_vida(jogador.saude, 100)}")
        print("-"*60)
        print("1. Atacar")
        print("2. Defender")
        print("3. Inventário")
        print("4. Sair")
        acao = input("Ação: ")

        if acao == "1":
            jogador.atacar(inimigo)
        elif acao == "2":
            print(f"{inimigo.nome} ataca {jogador.nome}, causando {inimigo.dano} de dano!")
            jogador.defender(inimigo.dano)
        elif acao == "3":
            vida_antes = jogador.saude  # <-- define aqui
            consultar_inv(jogador.inventario, jogador)
            
            if jogador.saude > vida_antes:
                continue  # jogador se curou, então o inimigo não ataca
        elif acao == "4":
            print("Você fugiu da batalha.")
            return

        if inimigo.esta_vivo() and acao != "2":  # "2" é a ação de defender
            inimigo.atacar(jogador)

    if jogador.esta_vivo():
        print(f"\nVocê derrotou {inimigo.nome} e ganhou {inimigo.recompensa}G!")
        jogador.dinheiro += inimigo.recompensa
    else:
        print("\nVocê foi derrotado...")

def main():
    jogador = Cavaleiro("Cavaleiro", dano=20, armadura="Escudo", resistencia=85)
    jogador.dinheiro = 100
    jogador.inventario = []
    loja = Loja()
    ferreiro = Ferreiro()
    estalagem = Estalagem()

    while True:
        escolha = mostrar_menu_principal(jogador)
        if escolha == "1":
            inimigo = escolher_inimigo()
            batalha(jogador, inimigo)
            if not jogador.esta_vivo():
                print("\nVocê morreu! Fim de jogo.")
                break  # Sai do loop principal do jogo
        elif escolha == "2":
            limpar_tela()
            loja.listar_pocoes()
            try:
                escolha_pocao = int(input("Escolha a poção para comprar: "))
                loja.vender_pocao(jogador, escolha_pocao)
            except ValueError:
                print("Entrada inválida.")
        elif escolha == "3":
            limpar_tela()
            ferreiro.listar_itens()
            try:
                escolha_item = int(input("Escolha o item para comprar: "))
                ferreiro.vender(jogador, escolha_item)
            except ValueError:
                print("Entrada inválida.")
        elif escolha == "4":
            estalagem.descansar(jogador)
        elif escolha == "5":
            consultar_inv(jogador.inventario, jogador)
        elif escolha == "6":
            print("Saindo do jogo...")
            break
        else:
            print("Escolha inválida.")

if __name__ == "__main__":
    main()
