from jogadores.cavaleiro import Cavaleiro
from inimigos.chefe import Boss
from npcs.loja_pocoes import Loja
from npcs.ferreiro import Ferreiro
from inimigos import minion

def barra_vida(atual, maximo):
    barras = 20
    preenchido = int(atual / maximo * barras)
    return '[' + '='*preenchido + ' '*(barras-preenchido) + f'] {atual}/{maximo}'

def combate(jogador, boss):
    while jogador.esta_vivo() and boss.esta_vivo():
        print(f"\nSua vida: {barra_vida(jogador.saude, jogador.vida_maxima)}")
        print(f"Vida do {boss.nome}: {barra_vida(boss.vida, boss.vida)}")
        acao = input("Atacar (a), Usar poção (p): ").lower()
        if acao == 'a':
            jogador.atacar(boss)
        elif acao == 'p':
            if jogador.inventario:
                for idx, item in enumerate(jogador.inventario, 1):
                    print(f"{idx}. {item.nome} ({item.tipo})")
                escolha = int(input("Escolha qual poção usar: ")) - 1
                item = jogador.inventario.pop(escolha)
                item.usar(jogador)
            else:
                print("Você não tem poções!")
                continue
        if boss.esta_vivo():
            boss.atacar(jogador)
    if jogador.esta_vivo():
        print(f"Você derrotou {boss.nome} e ganhou {boss.recompensa} de ouro!")
        jogador.dinheiro += boss.recompensa
        return True
    else:
        print("Você foi derrotado!")
        return False

def menu(jogador, loja, ferreiro):
    while True:
        print("\n--- MENU ---")
        print(f"Ouro: {jogador.dinheiro}")
        print("1. Comprar poção")
        print("2. Comprar arma/armadura")
        print("3. Enfrentar o último boss")
        print("4. Sair do jogo")
        escolha = input("O que deseja fazer? ")

        if escolha == '1':
            loja.listar_pocoes()
            po = int(input("Escolha a poção (0 para voltar): "))
            if po != 0:
                loja.vender_pocao(jogador, po)
        elif escolha == '2':
            ferreiro.listar_itens()
            it = int(input("Escolha o item (0 para voltar): "))
            if it != 0:
                ferreiro.vender(jogador, it)
        elif escolha == '3':
            return  # Sai do menu para enfrentar o boss
        elif escolha == '4':
            print("Você terminou sua jornada. Até a próxima!")
            exit()
        else:
            print("Escolha inválida.")

def main():
    jogador = Cavaleiro("Jogador", 20)
    jogador.vida_maxima = 100
    jogador.saude = 100
    jogador.dinheiro = 100
    jogador.inventario = []
    loja = Loja()
    ferreiro = Ferreiro()

    boss1 = Boss("Gárgula", 120, 18, 80)
    boss2 = Boss("Senhor das Cinzas", 180, 25, 200)

    # Enfrenta primeiro boss
    venceu = combate(jogador, boss1)
    if venceu:
        print(f"\nParabéns! Você derrotou {boss1.nome}.")
        print("(Dark Souls vibes) Você pode terminar sua jornada aqui ou tentar ficar mais forte para enfrentar o último boss.")
        escolha = input("Deseja tentar ficar mais forte antes do último boss? (s/n): ").lower()
        if escolha == "s":
            menu(jogador, loja, ferreiro)
        print("\nÉ hora do desafio final!")
        combate(jogador, boss2)
    else:
        print("Fim de jogo.")

if __name__ == "__main__":
    main()