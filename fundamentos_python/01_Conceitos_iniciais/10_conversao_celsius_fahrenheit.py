"""
RESUMO DE ENTRADA DE DADOS:
input() -> Para receber dados como texto (string)
int(input()) -> Para números inteiros
float(input()) -> Para números decimais
"""

# Recebe uma temperatura em graus Celsius e apresenta em Fahrenheit:
C = float(input("Digite uma temperatura em graus Celsius: "))
F = (9 * C + 160) / 5
print("A temperatura em graus Fahrenheit é: ", F)