#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
valor_Hora = float(input("Qual o valor hora? "))
num_Horas = int(input("Quantas horas trabalha em um dia? ")
dias_Trab = int(input("Quantos dias você trabalhou? "))

salario_Bruto = valor_Hora * num_Horas * dias_Trab

#descontos e o salário líquido
IR = float(salario_Bruto * 0.11)
INSS = float(salario_Bruto * 0.08)
sindicato = float(salario_Bruto * 0.05)
desconto = [IR, INSS, sindicato]
salario_Liq = salario_Bruto - sum(desconto)
print(f"O Salário Bruto é R$ {salario_Bruto}")
print(f"O salário mensal é R$ {salario_Liq}")