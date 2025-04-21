import sys
import os

# Adiciona a pasta 'lib' ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

from lib.personagem import PersonagemGame

# Instanciando dois personagens diferentes
heroi = PersonagemGame("Arthas", 10, 100, "Paladino")
vilao = PersonagemGame("Sylvanas", 12, 90, "Caçadora Sombria")

# Adicionando itens
heroi.adicionar_item("Espada de Luz")
vilao.adicionar_item("Arco das Sombras")

# Usando método atacar
heroi.atacar("Sylvanas")
vilao.atacar("Arthas")

# Imprimindo os dados
print("\n--- Dados dos Personagens ---")
print(vars(heroi))
print(vars(vilao))