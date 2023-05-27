print("------DESAFIO 38------")
print("----Detecção do maior valor----")

number01 = float(input("Primeiro número: "))
number02 = float(input("Segundo número: "))
listaNumeros = [number01, number02]

maior = 0

if max(listaNumeros) == number01:
    maior = 'PRIMEIRO'
elif max(listaNumeros) == number02:
    maior = 'SEGUNDO'

print(f"O {maior} valor é maior")
