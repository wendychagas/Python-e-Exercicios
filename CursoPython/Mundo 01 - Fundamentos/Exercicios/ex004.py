#-------------------------------------------------------------
x = input('Digite algo: ') # input sem explicitar a var sempre retorna um str;
print('O tipo primitivo é:', type(x))
print('Só tem espaços?', x.isspace()) # <objeto>.(método)
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está em maiúsculas?', x.isupper())
print('Está em minúsculas?', x.islower())
print('Está capitalizada?', x.istitle())
#-------------------------------------------------------------