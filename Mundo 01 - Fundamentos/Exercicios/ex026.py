frase = str(input('Digite a frase: ').upper()).strip()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase[0:].find("A")+1}')
print(f'A última letra A apareceu na posição {frase.rfind("A")+1}')
