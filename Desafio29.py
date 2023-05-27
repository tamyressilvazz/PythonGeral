
print("------DESAFIO 29------")
print("----Radar eletrônico----")

velocidade = float(input("Qual a velocidade atual do carro? "))
multa = 0
if velocidade > 80:
    print(f"MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    multa = (velocidade - 80) * 7
    print(f"Você deve pagar uma multa de R${multa}!")
elif velocidade <= 80:
    print(f"{velocidade}Km/h é uma velocidade permitida")
    print("Você não tem multas!")
print("Tenha um bom dia! Dirija com Segurança!")