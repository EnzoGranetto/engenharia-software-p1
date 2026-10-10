#Questão 3: A loja ELETROMÓVEIS está vendendo seus produtos no cartão em 5 parcelas sem juros. Escreva um programa em Python que receba o valor total da compra e calcule o valor de cada parcela.

#Entrada de dados
valor = float(input("Qual o valor total da compra?"))

#cálculo para 5 parcelas
parcela = valor/5

#Saída de dados
print(f"Cada parcela é de R${parcela:.2f} reais.")