'''
for tb realiza repetições "repita este bloco de código x vezes de forma automática"
A função range gera uma sequência de passos para o for percorrer for (para cada) x (variável) in range(número de sequência de repetições)
'''

#Exemplo:
#João comprou 5 produtos. Faça um programa que peça o preço dos cinco produtos e, ao final, apresente quanto ele gastou.

#Total gasto
total = 0

#repetir 5 vezes
for x in range(1,6):
  preco = float(input(f"Insira o preço do {x}º produto:"))
  total = total + preco
print(f"O total é R${total:.2f} reais")