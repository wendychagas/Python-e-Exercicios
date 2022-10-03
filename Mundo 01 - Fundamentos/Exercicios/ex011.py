#-------------------------------------------------------------
largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
area = largura*altura
rendimentoTinta = float(input('Rendimento da tinta: '))
print(f'Dimensão da parede = {largura}x{altura}\nÁrea = {area}m²\nQtnd tinta necessária = {area/rendimentoTinta}l')
#-------------------------------------------------------------