
print("------DESAFIO 33------")
print("----Maior e Menor valor----")

valor1 = float(input("Primeiro valor: "))
valor2 = float(input("Segundo valor: "))
valor3 = float(input("Terceiro valor: "))

valores = [valor1, valor2, valor3]

menor = min(valores)
maior = max(valores)

print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")