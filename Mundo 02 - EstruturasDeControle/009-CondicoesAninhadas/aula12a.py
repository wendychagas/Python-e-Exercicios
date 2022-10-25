nome = str(input('Qual é o seu nome? '))
if nome == 'Wendy':
    print(f'Que nome bonito! \033[0;34m{nome}\033[m!')
elif nome == 'João' or nome == 'Maria':
    print('Que nome \033[2;31mlegal\033[m!')
elif nome in 'Ana, Cláudia, Júlia, Jéssica, Isa':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal...')
print(f'Tenha um bom dia \033[0;33m{nome}\033[m!')

