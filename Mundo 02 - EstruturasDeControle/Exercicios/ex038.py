"""Ler 3 valores e verificar:
- o maior valor
- o menor valor
- se são iguais
"""

v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
v3 = int(input('Digite o 3º valor: '))
maior = v1
menor = v1
if v1 == v2 and v2 == v3 and v1 == v3:
    print(f'\nSão iguais\nV1: {v1}\nV2: {v2}\nV3: {v3}\n')
else:
    if menor > v2:
        menor = v2
    if menor > v3:
        menor = v3
    if maior < v2:
        maior = v2
    if maior < v3:
        maior = v3
    print(f'\nMaior: {maior}\nMenor: {menor}\n')