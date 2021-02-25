'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

numeros = []
while len(numeros) < 3:
    numeros.append(float(input("Informe um número: ")))

numeros.sort(reverse=True)
print(numeros)
