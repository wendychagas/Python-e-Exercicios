n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'Sua média foi {m:.2f}')
if m >= 7.0:
    print('Parabéns! Aprovado.')
else:
    print('Recuperação.')