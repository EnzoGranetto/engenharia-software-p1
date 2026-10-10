#Questão 10: Uma turma de Engenharia de Software realizará uma visita técnica a uma empresa. Para participar da atividade, o estudante deverá atender a alguns requisitos. Escreva um programa em Python que receba: a idade do estudante; a média acadêmica; a quantidade de faltas; se o estudante possui autorização dos responsáveis (S ou N); se o estudante possui alguma pendência com a instituição (S ou N). O estudante poderá participar da visita técnica se atender a uma das seguintes situações: possuir 18 anos ou mais, média maior ou igual a 6,0 e ter no máximo 10 faltas; OU possuir idade entre 16 e 17 anos, média maior ou igual a 6,0, ter no máximo 10 faltas e possuir autorização dos responsáveis. Além disso, em qualquer uma das situações, o estudante não poderá possuir pendências com a instituição. Ao final, o programa deverá informar se “O estudante está autorizado a participar da visita técnica” ou “O estudante não está autorizado a participar da visita técnica”.


#Entrada de dados
idade = int(input("Qual a sua idade? "))
media = float(input("Qual a sua média acadêmica? "))
faltas = int(input("Quantas vezes você faltou? "))
pendencia = input("Você possui alguma pendência com a instituição?(com S ou N) ")

#+18
if idade>=18:
  if media <6:
    print("O estudante não está autorizado a participar da visite técnica.")
  else:
    if faltas>10:
      print("O estudante não está autorizado a participar da visite técnica.")
    else:
      if pendencia == "S":
        print("O estudante não está autorizado a participar da visite técnica.")
      else:
        print("O estudante está autorizado a participar da visita técnica")
#-18
elif idade>15 and idade<18:
  if media<6:
    print("O estudante não está autorizado a participar da visite técnica.")
  else:
    if faltas>10:
      print("O estudante não está autorizado a participar da visite técnica.")
    else:
      autorizacao = input("Você possui autorização dos responsáveis?(com S ou N): ")
      if autorizacao == "N":
        print("O estudante não está autorizado a participar da visite técnica.")
      else:
        if pendencia == "S":
          print("O estudante não está autorizado a participar da visite técnica.")
        else:
          print("O estudante está autorizado a participar da visita técnica")
