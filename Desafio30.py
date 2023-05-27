
print("------DESAFIO 30------")
print("----Par ou Ímpar?----")

numero = int(input("Me diga um número qualquer: "))
paridade = 0
if numero % 2 == 0:
    paridade = 'Par'
    print(f"O número {numero} é {paridade}")
elif numero % 2 == 1:
    paridade = 'Ímpar'
    print(f"O número {numero} é {paridade}")