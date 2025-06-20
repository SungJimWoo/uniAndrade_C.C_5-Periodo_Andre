from itens import Pocao, Arma, Armadura

def main():
    faca = Arma("Tramontina")
    (faca.usar())

    phd = Pocao("Phd de Deslizamento")
    (phd.usar())

    blindagem = Armadura("Blindagem Máxima")
    (blindagem.usar())

if __name__ == "__main__":
    main()