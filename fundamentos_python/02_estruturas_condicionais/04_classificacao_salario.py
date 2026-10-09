#condicionais compostas -> 2 comparações com 1 variável
""""
EXERCÍCIO: CLASSIFICAÇÃO DE SALÁRIO
Ajuste das faixas salariais e correção de valores abaixo do limite mínimo.
"""

x = float(input("Qual o valor do seu salário? "))

if x < 1500:
    print("Melhor arranjar um emprego melhor")
elif x <= 5000:
    print("Pode melhorar")
else:
    print("Está bem de vida!")