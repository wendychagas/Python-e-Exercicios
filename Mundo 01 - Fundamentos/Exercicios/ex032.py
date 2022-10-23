from datetime import date
print('-=-' * 10)
tit = 'Ano Bissexto'
print(f'{tit:^30}')
print('-=-' * 10)
ano = int(input('Digite o ano Ou [0] para ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO.')