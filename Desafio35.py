
print("------DESAFIO 35------")
print("----Analisando Triângulo v1.0----")

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

"""Condições para um triângulo"""
cond1 = (b - c) * -1
conda_1 = b + a

cond2 = b - a
cond_2 = b + a

cond3 = a - c
cond_3 = a + c

if cond1 < a < conda_1 and cond2 < c < cond_2 and cond3 < b < cond_3:
    print(f"Os segmentos acima PODEM FORMAR um triângulo!")
else:
    print(f"Os segmentos acima NÃO PODEM FORMAR um triângulo!")