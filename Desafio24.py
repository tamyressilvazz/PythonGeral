print("------DESAFIO 24------")
print("----Verificando as primeiras letras de um texto----")

cidade = input("Digite o nome de uma cidade: ").strip()
divisor = cidade.split()
tam = len(divisor)

if tam >= 1:
    if divisor[0].upper() == 'SANTO':
        print(f"\tA cidade {cidade}, começa com Santo!!!")
    elif cidade[:5].upper() == 'SANTO':
        print(f"\tA cidade {cidade}, começa com Santo!!!")
    else:
        print(f"\tA cidade {cidade}, não começa com Santo")

