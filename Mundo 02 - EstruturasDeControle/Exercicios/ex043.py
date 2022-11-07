"""Exercício Python 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:

- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 24,9: Peso Ideal
- Entre 25 e 29,9: Sobrepeso
- Entre 30 e 34,9: Obesidade I
- Entre 35 e 39,9: Obesidade II (Severa)
- Acima de 40: Obesidade III (Mórbida)
"""

tit = 'I M C'
print('==' * 10)
print(f'{tit:^20}')
print('==' * 10)

altura = float(input('Altura (Cm): '))
peso = float(input('Peso (Kg): '))
imc = peso / ((altura / 100) ** 2)
print(f'IMC: {imc:.2f}\n')
tit = 'STATUS'
print('==' * 10)
print(f'{tit:^20}')
print('==' * 10)
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.50 and imc <= 24.99:
    print('Peso ideal.')
elif imc >= 25 and imc <= 29.99:
    print('Sobrepeso.')
elif imc >= 30 and imc <= 34.99:
    print('Obesidade I.')
elif imc >= 35 and imc <= 39.99:
    print('Obesidade II (Severa).')
elif imc >= 40:
    print('Obesidade III (Mórbida).')

