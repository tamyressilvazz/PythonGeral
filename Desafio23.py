print("------DESAFIO 23------")
print("----Separando dígitos de um número----")

print("Digite um número entre 0 e 9999")
num = input("Informe um número: ")

aux = list(str(num))
tam = len(aux)

print(f"\tAnalisando o número {num}...")
if tam == 4:
    unidade = aux[3]
    dezena =  aux[2]
    centena = aux[1]
    milhar = aux[0]
elif tam == 3:
    unidade = aux[2]
    dezena = aux[1]
    centena = aux[0]
    milhar = 0
elif tam == 2:
    unidade = aux[1]
    dezena = aux[0]
    centena = 0
    milhar = 0
elif tam == 1:
    unidade = aux[0]
    dezena = 0
    centena = 0
    milhar = 0
else:
    unidade = 0
    dezena = 0
    centena = 0
    milhar = 0

print(f"\tUnidade: {unidade}\n\tDezena: {dezena}\n\tCentena: {centena}\n\tMilhar: {milhar}")