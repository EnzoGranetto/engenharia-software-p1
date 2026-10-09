'''
Programa para classificar as notas
Solicite uma nota entre 0 e 10
Classifiquem as notas válidas
'''

n = float(input("Digite sua nota: "))

if n <0 or n>10:
  print("Nota inválida.")

elif n>=7 or n==10:
  print("Aprovado!")

elif n>=5 and n<=6.9:
  print("Você está de recuperação.")

else:
  print("Reprovado.")
