#-------------------------------------------------------------
n = float(input('1) Digite um valor: ')) # converte p/ float; mostra o tipo;
print(n, type(n))
#-------------------------------------------------------------
n = str(input('2) Digite um valor: ')) # converte p/ string; mostra o tipo;
print(n, type(n))
#-------------------------------------------------------------
n = bool(input('3) Digite um valor: ')) # se tem um valor dentro é True, se nao é False;
print(n, type(n))
#-------------------------------------------------------------
n = input('4) Digite algo: ') #sem declarar: por default == string;
print(n.isnumeric()) # é numérico?
print(n.isalpha()) # é alfabético?
print(n.isalnum()) # é alfanumérico?
print(n.isupper()) # é somente letras Maiúsculas?
#-------------------------------------------------------------






