'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

numeros = []        #cria a lista numeros
while len(numeros) < 3:         #enquanto o comprimento de numeros for menor que 3, faça
    numeros.append(float(input("Informe um número: ")))     #salvando o valor que o usuário digitou na lista numeros

numeros.sort(reverse=True)      #coloca a lista em decrescente
print(numeros)                  #imprime os números de forma decrescente, porém em forma de lista
