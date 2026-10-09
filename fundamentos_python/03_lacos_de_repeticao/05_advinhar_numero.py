#Solicite um número ao usuário e verifique se ele é igual a 5. Caso seja diferente de 5, o programa deverá solicitar um número novo. O processo deve REPETIR até que o usuário digite o número 5

x=5

numero = int(input("Digite um número: "))
if numero!=5:
  while True:
    numero = int(input("Digite um novo número: "))
    if numero == 5:
      break