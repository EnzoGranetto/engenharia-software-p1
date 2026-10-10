#Questão 8: A loja ELETROMÓVEIS está vendendo seus produtos no cartão de forma parcelada. Escreva um 1 programa em Python que receba o valor total da compra e o número de parcelas. Caso o número deparcelas seja maior que 10, deverá ser acrescentado R$ 30,00 ao valor total da compra. Ao final, o programa deverá calcular e apresentar o valor de cada parcela.

#Entrada de dados:
valor = float(input("Qual foi o valor total da compra? "))
parcela = int(input("Qual o número de parcelas desejadas? "))

#Condição
if parcela > 10:
  valor_com_juros = valor + 30
  print(f"Você pagará {parcela} parcelas de R${valor_com_juros/parcela :.2f} reais cada.")

else:
  print(f"Você pagará {parcela} parcelas de R${valor/parcela :.2f} reais cada.")