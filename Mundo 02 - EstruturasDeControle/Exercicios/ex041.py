"""Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

from datetime import date

data_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = data_atual - ano_nascimento
print(f'\nAno atual: {data_atual}')
print(f'Sua idade: {idade}\n')
if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Júnior')
elif idade <= 25:
    print('Categoria: Sênior')
elif idade > 25:
    print('Categoria: Master')

