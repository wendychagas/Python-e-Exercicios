import math

'''catetoOposto = float(input("comprimento do cateto oposto: "))
catetoAdjacente = float(input("Cateto adjacente: "))
hip = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print(f"A Hipotenusa = {hip:.2f}")'''

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hip = math.hypot(co, ca)
print(f"A hipotenusa = {hip:.2f}")


