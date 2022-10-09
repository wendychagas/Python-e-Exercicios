from math import trunc

numero = float(input("Digite um número real: "))
print(f"O valor {numero} truncado é = {trunc(numero)} - Usando f no inicio e módulo;;")
print("O valor {} truncado é = {} - Usando .format;".format(numero, trunc(numero)))
print(f"O valor {numero} truncado é = {int(numero)} - Usando f no inicio int();")


