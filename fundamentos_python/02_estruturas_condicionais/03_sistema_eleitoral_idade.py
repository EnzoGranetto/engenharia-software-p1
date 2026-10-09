'''
Escreva um programa que solicite a idade do usuário e determine sua situação em relação ao voto
-menor que 16 não votam
-pessoas com 16 ou 17 anos têm voto opcional
-pessoas de 18 a 70 anos têm voto obrigatório
- +70 anos tem voto opcional
-utilize if, elif e else para implementar a solução


x = int(input("Qual a sua idade? "))
if x < 16:
  print("Você não vota.")
elif x == 16 or x==17:
  print("Seu voto é opcional.")
elif x>=18 and x<=70:
  print("Seu voto é obrigatório")

else:
  print("Seu voto é opcional.")
'''
x = int(input("Qual a sua idade? "))
if x < 16:
  print("Você não vota.")

elif x<18:
  print("Seu voto é opcional.")

elif x<=70:
  print("Seu voto é obrigatório")

else:
  print("Seu voto é opcional.")