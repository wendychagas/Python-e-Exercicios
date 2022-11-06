"""Exercício Python 37:
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal"""

num = int(input('Valor decimal: '))
print("""
[ 1 ] - converter para BINÁRIO
[ 2 ] - converter para OCTAL
[ 3 ] - converter para HEXADECIMAL""")
op = int(input('[   ] - '))
if op == 1:
    print(f'\nDecimal: {num}\nBinário: {bin(num)[2:]}\n')
elif op == 2:
    print(f'\nDecimal: {num}\nOctal: {oct(num)[2:]}\n')
elif op  == 3:
    print(f'\nDecimal: {num}\nHexadecimal: {hex(num)[2:]}\n')
else:
    print('Opção inválida.')
