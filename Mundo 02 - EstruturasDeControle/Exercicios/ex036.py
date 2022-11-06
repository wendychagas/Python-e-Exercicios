"""
Exercício Python 36:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_casa = float(input('Qual o valor da casa? R$'))
salario_comprador = float(input('Qual salário do comprador? R$'))
anos_pagar = int(input('Em quantos anos de financiamento? '))
prestacao = valor_casa / (anos_pagar * 12)
minimo = salario_comprador * 30 / 100
print(f'\nValor casa: R${valor_casa}\nSalário: R${salario_comprador:.2f}\nFinanciamento: {anos_pagar} anos')
print(f'Prestação: {prestacao:.2f}\n')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO.')
else:
    print('Empréstimo NEGADO.')