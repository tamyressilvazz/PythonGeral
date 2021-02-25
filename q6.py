import math
print("PROGRAMA INICIANDO.........")
peso_Peixes = float(input("Insira o quilo de peixe: "))
print("***********CALCULANDO MULTAS***************")
if peso_Peixes == 50:
    print("O peso de peixes é 50 Kg, limite não ultrapassado")
else:
    excesso_Peso = peso_Peixes - 50
    multa_excesso = excesso_Peso * 4
    print(f"O peso de peixes é {peso_Peixes} Kg")
    print(f"-Você ultrapassou o limite\n-Multa = {math.ceil(multa_excesso)}")