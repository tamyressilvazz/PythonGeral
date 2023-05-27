'''
Ler duas notas de um aluno. calcule e mostre as notas
'''
print("==========Desafio 07==========")
print("--------MÉDIA DE DUAS NOTAS--------")

notas = []
notas.append(float(input("Primeira nota: ")))
notas.append(float(input("Segunda nota: ")))

media = sum(notas)/len(notas)
print(f"\tMÉDIA: {media}")