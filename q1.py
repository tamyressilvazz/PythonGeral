1.#Faça um Programa que peça dois números e imprima a soma.

numeros = []
numeros.append(float(input("Digite um número: ")))
numeros.append(float(input("Digite um número: ")))

result_soma = sum(numeros)
print(f"A soma dos números {numeros} é igual a {result_soma} ")
