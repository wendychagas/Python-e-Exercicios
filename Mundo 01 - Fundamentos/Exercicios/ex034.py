sal = float(input('Qual o seu salário R$'))
if sal > 1250.00:
    aumento = (sal * 10) / 100
    novoSal = sal + aumento
    print(f'Seu salário era R${sal:.2f} e agora é R${novoSal:.2f}')
    print(f'10% de aumento é = R${(novoSal-sal):.2f}')
else:
    aumento = (sal * 15) / 100
    novoSal = sal + aumento
    print(f'Seu salário era R${sal:.2f} e agora é R${novoSal:.2f}')
    print(f'15% de aumento é = R${(novoSal-sal):.2f}')