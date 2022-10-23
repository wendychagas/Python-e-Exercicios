from random import randint
from time import sleep

num_comp = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0-5. Tente adivinhar...')
print('-=-' * 20)
num = int(input('Em qual número pensei? '))
print('PROCESSANDO...')
sleep(2)
print(f'Pensei no número {num_comp}')
if num == num_comp:
    print('Parabéns! Você venceu.')
else:
    print('O computador venceu.')

