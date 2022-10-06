salarioAtual = float(input('Salario atual R$'))
taxaAumento = float(input('Informe a taxa de aumento %'))
valorAumento = salarioAtual * taxaAumento / 100
print(f'Seu novo salário com {taxaAumento:.2f}% de aumento é de R${salarioAtual+valorAumento:.2f}')
print(f'Recebeu um aumento de R${valorAumento:.2f}')