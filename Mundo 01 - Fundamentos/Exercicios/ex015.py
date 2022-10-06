kmPercorridos = float(input('Quantos Km foram percorridos: '))
diasPassados = float(input('Por quantos dias: '))
valorKm = 0.15
valorAluguel = 60
totPagar = (kmPercorridos * valorKm) + (valorAluguel * diasPassados)
print(f'Total a pagar é R${totPagar:.2f}')

# método por entrada do usuário

precoKilometro = float(input('Preço do Km R$'))
kmAndados = float(input('Quantos Km foram percorridos: '))
precoAluguel = float(input('Preço da diária R$'))
totalDias = float(input('Quantos dias: '))
print(f'Total à pagar R${(precoKilometro * kmAndados) + (precoAluguel * totalDias):.2f}')




