"""Exercício Python 39:
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

data_atual = date.today().year
tit = 'Alistamento'
print('==' * 10)
print(f'{tit:^20}')
print('==' * 10)
print("""
[ M ] - Masculino
[ F ] - Feminino
[ X ] - Outros""")
op = input('[   ] - ')
if op.upper() == 'M':
    ano_nascimento = int(input('Ano de nascimento: '))
    idade = data_atual - ano_nascimento
    print(f'\nAno atual: {data_atual}\nNascimento: {ano_nascimento}\nIdade: {idade} anos\n')
    if idade == 18:
        print(f'Com {idade} anos de idade deve se alistar ao Serviço Militar IMEDIATAMENTE.')
    elif idade < 18:
        resta = 18 - idade
        print('Não completou 18 anos.')
        print(f'Faltam {resta} anos para o alistamento.')
        ano = data_atual + resta
        print(f'Seu alistamento será em {ano}.')
    elif idade > 18:
        passou = idade - 18
        print('Passou dos 18 anos.')
        print(f'Deveria ter se alistado há {passou} anos.')
        ano = data_atual - passou
        print(f'Seu alistamento foi em {ano}.')
elif op.upper() == 'F' or op.upper() == 'X':
    resp = input('Deseja se alistar ao Serviço Militar?\n[ S ] - sim\n[ N ] - não\n[   ] - ')
    if resp.upper() == 'N':
        pass
    elif resp.upper() == 'S':
        ano_nascimento = int(input('Ano de nascimento: '))
        idade = data_atual - ano_nascimento
        print(f'\nAno atual: {data_atual}\nNascimento: {ano_nascimento}\nIdade: {idade} anos\n')
        if idade == 18:
            print(f'Com {idade} anos de idade deve se alistar ao Serviço Militar IMEDIATAMENTE.')
        elif idade < 18:
            resta = 18 - idade
            print('Não completou 18 anos.')
            print(f'Faltam {resta} anos para o alistamento.')
            ano = data_atual + resta
            print(f'Seu alistamento será em {ano}.')
        elif idade > 18:
            passou = idade - 18
            print('Passou dos 18 anos.')
            print(f'Deveria ter se alistado há {passou} anos.')
            ano = data_atual - passou
            print(f'Seu alistamento foi em {ano}.')

