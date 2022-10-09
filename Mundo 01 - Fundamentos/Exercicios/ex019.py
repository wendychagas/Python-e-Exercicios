import random

print("--" * 10)
titulo = "Sorteio"
print(f"{titulo:^20}")
print("--" * 10)
nome1 = input("1º Aluno(a): ")
nome2 = input("2º Aluno(a): ")
nome3 = input("3º Aluno(a): ")
nome4 = input("4º Aluno(a): ")
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

print(f"Sorteado(a) foi {escolhido}!")
