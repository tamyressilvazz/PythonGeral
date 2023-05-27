
print("------DESAFIO 34------")
print("----Aumentos Múltiplos----")

salario = float(input("Qual é o salário do funcionário? R$"))

taxa = 0
if salario > 1250.00:
    taxa = 1.10
elif salario <= 1250.00:
    taxa = 1.15

aumento = salario * taxa

print(f"Quem ganhava R${salario} passa a ganhar R${aumento}")