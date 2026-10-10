#Questão 2: Escreva um programa em Python que leia o nome de um vendedor, o seu salário fixo e o valor total das vendas realizadas no mês. Sabendo que o vendedor recebe uma comissão de 15% sobre o valor total de suas vendas.

#Entrada de dados
nome = input("Qual seu nome?")
salario = float(input("Qual é o seu salário fixo?"))
vendas = float(input("Qual foi o valor total das vendas realizadas no mês?"))

#comissão de 15% do total de vendas
comissao = vendas * 0.15

#Saída de dados
print(f"O vendedor {nome} receberá R${salario + comissao :.2f} esse mês")