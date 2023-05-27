print("------DESAFIO 25------")
print("----Procurando uma string dentro de outra----")

nome_Completo = input("Qual é o seu nome completo? ").upper()

existe = nome_Completo.find('SILVA')

if existe >= 1:
    resposta = True
else:
    resposta = False
print(f"Seu nome tem Silva? {resposta}")