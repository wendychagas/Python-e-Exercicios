from random import randint #importando função randint da biblioteca random

print("--" * 10)
titulo2 = "Adivinhação"
print(f"{titulo2:^20}")
print("--" * 10)
sorteio = randint(0, 100)
tentativas = 1
acertou = False
while acertou == False:
  numero = int(input("Escolha um número entre 0-100: --> "))
  if numero == sorteio:
    print(f"O número sorteado foi {sorteio}!")
    print("Parabéns! Você acertou com {} tentativas.\n".format(tentativas))
    acertou = True
  else:
    if numero > sorteio:
      print("O número sorteado é menor que {}\n".format(numero))
    else:
      print("O número sorteado é maior que {}\n".format(numero))
  tentativas = tentativas + 1
