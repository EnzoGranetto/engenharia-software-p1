#Questão 9: Escreva um programa em Python que receba o salário-base de um funcionário, calcule o valor do imposto de acordo com a tabela apresentada e, ao final, mostre o valor do imposto a ser pago.
'''
- Menor que R$ 200: Isento (0% de imposto)
- Até R$ 450: 3% de imposto
- Menor que R$ 700: 8% de imposto
- Acima de R$ 700: 12% de imposto
'''

# Entrada de dados
x = float(input("Qual é o seu salário base? "))

# Condição
if x < 200:
    resultado = 0  
elif x <= 450:
    resultado = x * 0.03
elif x < 700:
    resultado = x * 0.08
else:
    resultado = x * 0.12

# Saída de dados
print(f"Você pagará R${resultado:.2f} de imposto")


