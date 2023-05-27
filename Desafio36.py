
print("------DESAFIO 36------")
print("----Aprovando Empréstimo----")

valorCasa = float(input("Qual o valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anosPg = int(input("Quantos anos de financiamento? "))

parcela = valorCasa / (anosPg * 12)
valorMin = salario * 30 / 100

print(f"Para pagar uma casa de R${valorCasa} em {anosPg} anos ", end='')
print(f"a prestação será de R${parcela}")
if parcela <= valorMin:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print('Empréstimo NEGADO!')