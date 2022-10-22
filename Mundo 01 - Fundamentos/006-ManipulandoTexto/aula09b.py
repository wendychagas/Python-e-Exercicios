frase = 'Curso em Vídeo Python'
frase2 = '     Curso em Vídeo Python    '

print(f'Mostrar frase: {frase}')
print(f'Fatiar [3:13]: {frase[3:13]}')
print(f'Fatiar [0:13]: {frase[:13]}')
print(f'Fatiar [13:]: {frase[13:]}')
print(f'Fatiar [1:15]: {frase[1:15]}')
print(f'Fatiar [1:12]: {frase[1:12:2]}')
print(f'Fatiar [1::2]: {frase[1::2]}')
print(f'Fatiar [::2]: {frase[::2]}')
print(f'Contando "o" -> {frase.count("o")}') # "o" != "O";
print(f'Contando "O" -> {frase.upper().count("O")}') # contando os "o" ou "O" jogando os "o" e "O" para MAIÚSCULO;
print(f'Comprimentro frase -> {len(frase)}')
print(f'Comprimento frase com espaços -> {len(frase2)}')
print(f'Removendo espaços indesejados -> {len(frase2.strip())}')
print(f'Substituindo palavras: {frase.replace("Python", "Android")}') # não substitui a frase;
# para substituir:
# frase = frase.replace("Python", "Android")
print("Tem palavra ´Curso´ na frase?", 'Curso' in frase)
print(f'´Curso´ na posição -> {frase.find("Curso")}')
print(f'´Vídeo´ na posição -> {frase.find("Vídeo")}')
print(f'´vídeo´ na posição -> {frase.find("vídeo")}')
print(f'´Vídeo´ em frase.lower().find("vídeo")  na posição -> {frase.lower().find("vídeo")}')
print(f'frase.split() -> {frase.split()}')
dividido = frase.split()
print(f'dividido = frase.split() -> {dividido}')
print(f'Posição [0] -> {dividido[0]}')
print(f'Posição [1] -> {dividido[1]}')
print(f'Posição [2] -> {dividido[2]}')
print(f'Posição [3] -> {dividido[3]}')
print(f'Pegar o item da lista[2] e o indice desse item[3] -> {dividido[2][3]}')
















