"""
usaremos nosso conhecimento de condicionais if,
elif e else para calcular uma tarifa de transporte compartilhado
*dependendo do tipo de viagem escolhido
"""

tipo_corrida = input("Digite a escolha de viagem: 'Black' ou 'DooberX' ").upper()
credito = float(input("Quanto de crédito você tem? "))

preco_corrida = 0
preco_final = 0

if tipo_corrida == "DOOBERX":
    preco_corrida = 20.5
elif tipo_corrida == "BLACK":
    preco_corrida = 37.9
else:
    preco_corrida = 18.7

if credito > 0:
    preco_final = credito - preco_corrida

print(f"O preço da corrida é {preco_corrida}")
print(f"Seu troco: {preco_final}")
