salarioAtual = float(input('Salario atual R$'))
taxaAumento = float(input('Informe a taxa de aumento %'))
valorAumento = salarioAtual * taxaAumento / 100
print(f'Seu novo salário com {taxaAumento:.2f}% de aumento é de R${salarioAtual+valorAumento:.2f}')
print(f'Recebeu um aumento de R${valorAumento:.2f}')

# Outra forma de resolver:

salario = float(input('Salário atual R$'))
desconto = float(input('Aumento de %'))
novoSalario = salario + (salario * desconto / 100)
print(f'Meu novo salário é de R${novoSalario:.2f}')
print(f'Recebeu um aumento de R${novoSalario - salario:.2f}')