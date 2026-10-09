"""
CONCEITOS DA AULA: OPERADORES ARITMÉTICOS
/   : Divisão com resultado decimal (float)
//  : Divisão inteira (despreza as casas decimais)
**  : Potenciação
%   : Resto da divisão (módulo)
()  : Parênteses para definir a ordem de precedência dos cálculos

"""


N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))

print("Adição: ", N1 + N2)
print("Subtração: ", N1 - N2)
print("Multiplicação: ", N1 * N2)
print("Potenciação: ", N1 ** N2)
print("Divisão: ", N1 / N2)
print("Divisão inteira: ", N1 // N2)
print("Resto: ", N1 % N2)