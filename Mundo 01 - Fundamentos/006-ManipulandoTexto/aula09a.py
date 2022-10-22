# Técnicas Manipulação de Texto

# Frase exemplo 1;
frase = 'Curso em Video Python' # cada espaço na string é um microespaço[] na memória principal;
# Frase exemplo 2;
frase2 = '   Aprenda Python  '

# -> Fatiamento;
print(frase[9]) # V != v; frase indice/posição 9[];
print(frase[9:13]) # do indice 9[] ate o 13[], sem contar o 13[]; Regra: ranges um a menos no final;
print(frase[9:21]) # frase só tem 20[]; indices maiores são válidos; não é boa prática;
print(frase[9:21:2]) # começa no 9, vou parar no 21, saltando de 2 em 2;
print(frase[:5]) # omitir o indice força começar do inicio, vai até o 5[] nesse caso;
print(frase[15:]) # começa do 15[] e vai até o fim;
print(frase[9::3]) # começa do 9[], vai até o final, saltando de 3 em 3;

# -> Análise de String;
# obter dados, quando começa, tamanho dela, qual letra começa/termina etc;
len(frase) # mostra o comprimento;
frase.count('o') # contar quantas vezes aparece a letra 'o' minúscula;
frase.count('o', 0, 13) # contagem de 'o' já com fatiamento; contar os 'o' de 0[] ate 13[] sem contar a 13[]
frase.find('deo') # mostra a posição que começa 'deo';
frase.find('Android') # uma string que não existe retorna posição -1[]; posição não existe;
'Curso' in frase # dentro da frase existe a palavra curso? retorna valor Booleano;

# Transformação;
# modificar com métodos;
frase.replace('Python', 'Android') # vai procurar por 'Python', e substituir por 'Android';
frase.upper() # método maiúsculas; frase ficou MAIÚSCULA;
frase.lower() # frase fica minúscula;
frase.capitalize() # TODOS caracteres minúsculos, APENAS o PRIMEIRO MAIÚSCULO;
frase.title() # onde estiver 'espaço' substiitui as primeiras em MAIÚSCULA;
frase2.strip() # remover espaços inúteis do inicio e do fim;
frase2.rstrip() # similar ao strip, variação r, funciona pela direita;
frase2.lstrip() # similar ao rstrip, variação l, funciona pela esquerda;

# Divisão;
frase.split() # divide cada palavra em uma indexação nova; gera basicamente uma lista; ['Curso', 'em', 'Video', 'Python']

# Junção;

'-'.join(frase) # juntar a cadeia de caracteres com hífen; Curso-em-Video-Python







