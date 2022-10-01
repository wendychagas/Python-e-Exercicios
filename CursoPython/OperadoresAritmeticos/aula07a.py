#-------------------------------------------------------------
nome = input('Qual é o seu nome: ')
print('Bem Vindo {:20}!'.format(nome)) # {:<valor de espaços>}
print('Bem Vindo {:>20}!'.format(nome)) # {:<valor de espaços .e.(input)à direita>}
print('Bem Vindo {:<20}!'.format(nome)) # {:<valor de espaços .e.(input) à esquerda>}
print('Bem Vindo {:^20}!'.format(nome)) # {:<valor de espaços .e.(input) centralizado>}
print('Bem Vindo {:~^20}!'.format((nome))) # {:<valor de espaços .e.'<caracter>'.e.(input) centralizado>}
#-------------------------------------------------------------
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
m = n1 * n2 # multiplicação
d = n1 / n2 # divisão
di = n1 // n2 # divisão inteira
p = n1 ** n2 # potência
print(f'A soma é = {n1+n2}') # Outra forma de print operadores;
print('A soma é = {}'.format(n1+n2)) # forma alternativa;
print('O produto é = {}'.format(m), end=' ') # fim da linha recebe qualquer string;
print('A divisão é = {:.3f}'.format(d)) # divisão formatada com apenas 3 casas decimais;
print('A divisão \n inteira é = {}'.format(di)) # \n quebra linha na posição desejada;
print('A potência é = {}'.format(p))
#-------------------------------------------------------------



