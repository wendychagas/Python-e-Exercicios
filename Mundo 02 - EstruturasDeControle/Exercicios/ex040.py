"""Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""
tit = 'Média'
print('==' * 10)
print(f'{tit:^20}')
print('==' * 10)

entrar = input('Pressione ENTER para iniciar\n')
soma_notas = 0
for i in range(1, 5):
    notas = float(input(f'{i}ª nota: '))
    soma_notas += notas
media = soma_notas / 4
if media  < 5:
    print('\nReprovado.')
elif media >= 5.0 and media < 6.9:
    print('\nRecuperação.')
elif media >= 7.0:
    print('\nAprovado.')
print(f'Média: {media:.2f}')