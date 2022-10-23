vel = int(input('Passou em qual velocidade: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Ultrapassou o limite de velocidade. Você foi multado.')
    print(f'Multa de R${multa:.2f}')
else:
    print('Tenha boa viagem.')

