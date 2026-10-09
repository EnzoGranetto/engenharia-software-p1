'''
Escreva um programa de login
solicite:
-nome do usuário
-senha

O acesso deverá ser permitido quando:
-usuario = admin
-senha = 1234
'''

while True:
    nome = input('Digite seu nome de usuário: ')
    senha = int(input('Digite sua senha: '))

    if nome == 'admin' and senha == 1234:
        print("Seu acesso está permitido.")
        break
    else:
        print("Usuário e/ou senha incorretos.")
