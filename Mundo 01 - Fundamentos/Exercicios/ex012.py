precoCusto = float(input('Qual o preço de custo R$'))
taxaDesconto = float(input('Qual a taxa de desconto %: '))
valorDesconto = precoCusto * taxaDesconto / 100
print(f'O preço do produto com {taxaDesconto}% de desconto foi de R${precoCusto-valorDesconto:.2f}')
print(f'Economia de R${valorDesconto:.2f}')

