print("------DESAFIO 22------")
print("----Analisador de Textos----")

nome_Completo = input("Digite seu nome completo: ")

maiuscula = nome_Completo.upper()
minuscula = nome_Completo.lower()

aux = nome_Completo.split()
aux = ''.join(aux)
tam1 = len(aux)

first = nome_Completo.split()
primeiro_Nome = first[0]
tam2 = len(primeiro_Nome)

print("\tAnalisando seu nome...")
print(f"\tSeu nome em maiúscula é {maiuscula}")
print(f"\tSeu nome em minúscula é {minuscula}")
print(f"\tSeu nome tem ao todo {tam1} letras")
print(f"\tSeu primeiro nome é {primeiro_Nome} e ele tem {tam2} letras")