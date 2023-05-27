print("------DESAFIO 31------")
print("----Custo da Viagem----")

distancia = float(input("Qual a distância da sua viagem?"))

print(f"Você está prestes a começar uma viagem de {distancia}Km.")
custo = 0
if distancia <= 200:
    custo = distancia * 0.50
elif distancia > 200:
    custo = distancia * 0.45
print(f"E o preço da sua passagem será de R${custo}")
