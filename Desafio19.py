import random

print("------DESAFIO 19------")
print("----Sorteando um item da lista----")

alunos = list()

'''Adicionando elementos na lista alunos'''
alunos.append(input("Primeiro aluno: "))
alunos.append(input("Segundo aluno: "))
alunos.append(input("Terceiro aluno: "))
alunos.append(input("Quarto aluno: "))

'''sorteando um item da lista alunos'''
sorteio = random.choice(alunos)

print("\tRESULTADO DO SORTEIO:")
print(f"\tO aluno escolhido foi {sorteio}")

