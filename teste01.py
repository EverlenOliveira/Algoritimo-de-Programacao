# Importação das bibliotecas necessárias
from random import randint

# Opções do jogo
items = ['Pedra', 'Papel', 'Tesoura']

# Variáveis para estatísticas do jogo
vitorias = 0
derrotas = 0
empates = 0

# Função para exibir um título estilizado
def print_titulo():
    print("=" * 36)
    print("          JOKENPÔ - BATALHA FINAL")
    print("=" * 36)

# Execução do jogo
while True:
    print_titulo()
    computador = randint(0, 2)  # Computador escolhe um número aleatório entre 0 e 2

    # Exibir opções para o jogador
    print("\nSuas opções:")
    for i, item in enumerate(items):
        print(f"[ {i} ] {item}")

    # Validação da jogada do usuário
    while True:
        try:
            jogador = int(input("\nQual a sua jogada? "))
            if jogador in [0, 1, 2]:
                break
            else:
                print("Opção inválida! Escolha 0, 1 ou 2.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    # Mostra escolhas
    print(f"\nComputador escolheu {items[computador]}")
    print(f"Você escolheu {items[jogador]}\n")

    # Regras do jogo
    if computador == jogador:
        print("EMPATE!")
        empates += 1
    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print("VOCÊ VENCEU!")
        vitorias += 1
    else:
        print("COMPUTADOR VENCEU!")
        derrotas += 1

    # Pergunta se deseja jogar novamente
    n = input("\nDeseja jogar novamente? [S/N] ").strip().upper()
    if n == 'N':
        print(f"\nPlacar Final:")
        print(f"Vitórias: {vitorias}")
        print(f"Derrotas: {derrotas}")
        print(f"Empates: {empates}")
        print("\nObrigado por jogar! Até a próxima!")
        break