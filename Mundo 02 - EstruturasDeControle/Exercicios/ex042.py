"""Exercício Python 042:
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:

- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print(f'\nSegmento 1: {r1}cm\nSegmento 2: {r2}cm\nSegmento 3: {r3}cm\n')
    print('PODEM formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print(f'\nSegmento 1: {r1}cm\nSegmento 2: {r2}cm\nSegmento 3: {r3}cm\n')
    print('NÃO PODEM formar um triângulo.')