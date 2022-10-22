# alternativa de resolver com matemática;
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade = {u}')
print(f'Dezena = {d}')
print(f'Centena = {c}')
print(f'Milhar = {m}')



"""n = num + 10000
nn = str(n)
print(f'A unidade é: {nn[-1]}')
print(f'A dezena é: {nn[-2]}')
print(f'A centena é: {nn[-3]}')
print(f'O milhar é: {nn[1]}')"""