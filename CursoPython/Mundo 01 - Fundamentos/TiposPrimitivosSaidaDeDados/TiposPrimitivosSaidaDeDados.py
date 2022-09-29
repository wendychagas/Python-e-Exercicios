print('Concatena')
n1 = input('Digite um número: ')
n2 = input('Digite mais um número: ')
s = n1 + n2 #essa linha concatena;
print('A soma vale ', s, '.')
#-------------------------------------------------------------
print('Soma')
n1 = int(input('Digite um número: ')) #tipo primitivo int;
n2 = int(input('Digite mais um número: ')) #tipo primitivo int;
s = n1 + n2 #essa linha soma;
print('A soma vale {}'.format(s))
#-------------------------------------------------------------
# int: | 7 | -4 | | 0 | 9875 |
# float: | 4.5 | 0.076 | -15.223 | 7.0 |
# bool: | True | False | ps: Inicial maiúscula;
# str: 'Olá' | "Olá" | '7.5' | "" | '' |
#-------------------------------------------------------------
print('A soma de', n1, 'e', n2, 'vale', s, '.')
print('A soma entre {0} + {1} = {2}.'.format(n1, n2, s))
print(f'{n1} + {n2} = {s}.')
#-------------------------------------------------------------














