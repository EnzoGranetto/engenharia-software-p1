#Solicite 10 notas ao usuário e , ao final, calcule e apresente a média aritmética das notas informadas.
total = 0

for x in range(1,11):
  nota = float(input(f"Qual a nota da {x}º prova? "))
  total = total + nota
print(f"Sua média aritmética é igual a {total /10} pontos.")