
# 🛡️ Projeto: Dark Souls (versão terminal)

Este é um jogo em modo texto, baseado no universo de **Dark Souls**, desenvolvido em Python como prática de Programação Orientada a Objetos.

---

## 👨‍💻 Autores

- **André Henrique Fiatkoski Lustosa**
- **Matias Julian Bulacio**

---

## 🎮 Funcionalidades

- Sistema de batalhas com inimigos aleatórios e chefes
- Inventário dinâmico (poções, armas, armaduras)
- NPCs interativos:
  - **Loja de Poções**
  - **Ferreiro** (compra de equipamentos)
  - **Estalagem** (cura)
- Equipamento e uso de itens durante e fora da batalha
- Gold e recompensas por vitórias

---

## 🗂️ Estrutura do Projeto

```
Python/
└── darkSouls/
    ├── games.py                  # Código principal do jogo
    ├── inimigos/                 # Chefes e inimigos normais
    │   ├── chefe.py
    │   ├── minion.py, minion1.py, ..., minion5.py
    ├── itens/                    # Todos os itens utilizáveis
    │   ├── arma.py
    │   ├── armadura.py
    │   ├── item.py
    │   ├── pocao.py
    ├── jogadores/                # Classes jogáveis
    │   ├── cavaleiro.py
    │   ├── jogador.py
    ├── npcs/                     # Personagens não jogáveis
        ├── estalagem.py
        ├── ferreiro.py
        ├── loja_pocoes.py
```

---

## ▶️ Como Rodar

1. Acesse o diretório do projeto:

```bash
cd Python/darkSouls
```

2. Execute o jogo:

```bash
python games.py
```

---

## 💡 Requisitos

- Python 3.10+
- Terminal que aceite `input()` para interação

---

## 🎯 Objetivo Educacional

Este projeto foi construído para desenvolver habilidades em:

- Programação Orientada a Objetos (POO)
- Estruturação modular com pacotes Python
- Lógica de RPG (turnos, buffs, inventário)
- Leitura e manipulação de atributos via terminal

---

## 📄 Licença

Projeto acadêmico livre para fins educacionais e aperfeiçoamento pessoal.
