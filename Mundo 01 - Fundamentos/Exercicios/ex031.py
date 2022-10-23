dist = float(input('Qual a distância da viagem? '))
if dist <= 200:
    precoPass = 0.50 * dist
else:
    precoPass = 0.45 * dist
print(f'Para viagem de {dist}Km vai pagar R${precoPass:.2f} na passagem.')
