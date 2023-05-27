print("==========Desafio 09==========")
print("--------LER INTEIRO E MOSTRAR A TABUADA DELE--------")

num = []
num = int(input("Digite o número: "))

tab_Num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("TABUADA DA MULTIPLICAÇÃO")
print("_______________________")
for tab_Num in tab_Num:
    multp = num * tab_Num
    print(f"\t{num} * {tab_Num} = {multp}")
print("_______________________")
