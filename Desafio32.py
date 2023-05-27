
print("------DESAFIO 32------")
print("----Ano Bissexto----")

ano = int(input("Que ano quer analisar? "))

if ano % 4 == 0 or ano % 400 == 0 and ano % 100 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é um ano Bissexto!")