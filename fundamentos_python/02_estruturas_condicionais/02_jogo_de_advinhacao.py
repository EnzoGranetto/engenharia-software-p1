"""
DESAFIO: JOGO DE ADIVINHAÇÃO
Escreva uma variável 'num' e atribua um valor inteiro entre 0 e 10.
Peça ao utilizador para tentar adivinhar o valor.
Se acertar, imprime "Você acertou!". Se errar, pede outro número até acertar.
"""

# Definindo o número secreto
num = 7

# --- VERSÃO COM REPETIÇÃO (WHILE) ---
while True:
    tentativa = int(input("Tente adivinhar o número de 0 a 10: "))

    if tentativa == num:
        print("Você acertou!")
        break  # Interrompe o loop quando o utilizador acerta
    else:
        print("Você errou! Escolha outro número.")