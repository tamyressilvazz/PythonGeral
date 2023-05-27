'''
Ler um num Real qualquer do teclado e mostrar na tela sua porção inteira
Ex.: Digite um número:
     O número digitado 6.785 tem parte inteira 6
'''
'''
Solução 01
num = float(input("Digite um número: "))
part_Int = int(num)

print(f"{num} tem parte inteira {part_Int}")
'''
#Solução 02
from math import trunc

print("\t\t-----DESAFIO 16-----")
print("******PARTE INTEIRA DE UM NÚMERO*******")

num = float(input("\tDigite um número: "))
part_Int = trunc(num)

print(f"\t{num} tem parte inteira {part_Int}")