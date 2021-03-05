'''
Considere a seguinte atribuição xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
Escreva um laço que imprima cada um dos números em uma nova linha.
Escreva um laço que imprima cada um dos números e seu quadrado em uma nova linha.
'''
numeros = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for numero in numeros:
    print(f"O número é {numero}")

for numero in numeros:
    print(f"O número é: {numero} e seu quadrado: {numero**2}")