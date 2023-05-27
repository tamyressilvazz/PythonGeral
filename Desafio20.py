import random
print("------DESAFIO 20------")
print("----Sorteando uma ordem na lista----")

'''Adicionando elementos na lista alunos'''
alu1 = input("Primeiro aluno: ")
alu2 = input("Segundo aluno: ")
alu3 = input("Terceiro aluno: ")
alu4 = input("Quarto aluno: ")
alunos = [alu1, alu2, alu3, alu4]

'''sorteando a ordem da lista alunos'''
random.shuffle(alunos)

print("\tRESULTADO DO SORTEIO")
print(f"\tA ordem de apresentação será: \n\t{alunos}")