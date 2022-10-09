import math # from math import sqrt | from math import sqrt, floor
# math = [ceil, floor, trunc, pow, sqr, factorial]

# ceil ==  arrendonda para cima;
# floor == arredonda para baixo;
# trunc == eliminar da virgula para frente;
# pow == potência;
# sqrt == square roots - raiz quadrada;
# factorial == fatorial;

numero = int(input("Digite um número: "))
raiz = math.sqrt(numero)
print(f"A raiz de {numero} = {raiz}")
print(f"A raiz de {numero} = {math.ceil(raiz)} (Arredonda para cima)")
print(f"A raiz de {numero} = {math.floor(raiz)} (Arredondado para baixo)")
print(f"A raiz de {numero} = {math.trunc(raiz)} (Truncada)")




