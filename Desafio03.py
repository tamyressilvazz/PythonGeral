print("=========Desafio 03=========")
print("-----SOMA ENTRE NÚMEROS-----")
numeros = []
numeros.append(float(input("Informe um número: ")))
numeros.append(float(input("Informe outro número: ")))
soma = sum(numeros)
print(f"A soma dos números {numeros[0]} + {numeros[1]} = {soma}")