#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
c = 1
while c < 5:
    notas = float(input("Digite a nota: "))
    c = c + 1

media_notas = (sum(notas))/len(notas)
print("***************************************")
print(f"A média das notas {notas} é {media_notas}")