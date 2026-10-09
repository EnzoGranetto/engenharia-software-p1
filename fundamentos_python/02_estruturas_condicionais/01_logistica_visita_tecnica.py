#A turma de Eng. de Software realizará uma visita técnica. Para transportar os estudantes, serão utilizadas *vans com capacidade para 15 pessoas*
#Escreva um programa que solicite : 1- Qtd. total de estudantes. 2-Qtd. de professores. 3-Capacidade de cada van. 4-Valor de aluguel de uma van. 5-valor disponível para custear o transporte
#O programa deverá calcular:
# a) Quantas vans ficarão completamente lotadas?
# b) Quantas pessoas ficarão para serem transportadas depois de preencher as vans completas?
# c) Quantas vans serão necessárias no total para transportar todas as pessoas?
# d) Quantas vagas ficarão vazias considerando todas as vans contratadas?
# e) Qual será o custo total do transporte?

#Estudantes: 67 , Professores: 4, Capacidade da van: 15 , Aluguel de cada van: R$650, Valor disponível: R$4k

estudantes = int(input("Qual a quantidade total de estudantes? "))
professores = int(input("Qual a quantidade de professores? "))
capacidade_van = int(input("Qual a capacidade de cada van? "))
aluguel_van = int(input("Quanto é o aluguel de uma van? "))
valor_disponível = float(input("Qual é o valor disponível para custear o transporte? "))

vans_lotadas = (estudantes + professores) // capacidade_van
print("a) Terão" ,vans_lotadas , "vans lotadas" )

resto_pessoas = (estudantes + professores) % capacidade_van
print("b)", resto_pessoas , "ficarão para serem transportadas depois de preencher as vans completas" )

if(resto_pessoas==0): print("c) Serão necessárias" ,vans_lotadas, "vans" )
else: print("c) Serão necessárias" ,vans_lotadas +1 ,"vans" )

if(resto_pessoas==0): print("d) Não terão vagas vazias")
else: print("d) Sobrarão" ,capacidade_van - resto_pessoas,"vagas vazias" )

if(resto_pessoas==0): print("e) O custo total será de: R$" ,vans_lotadas * aluguel_van, "reais" )
else: print("e) O custo total será de: ",(vans_lotadas +1)*aluguel_van ,"reais" )