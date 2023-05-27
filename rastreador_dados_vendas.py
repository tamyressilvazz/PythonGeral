"""Compararemos jeans_sold com a meta para ver se o varejista atingiu sua meta de vendas.
    Então vamos verificar se ainda há jeans em estoque.
"""

estoque = int(input("Quantidade de Jeans em estoque: "))
jeans_vendidos = int(input("Quantos jeans foram vendidos? "))
meta = int(input("Quantos jeans precisam ser vendido para bater a meta? "))

estoque_atual = False

if jeans_vendidos == meta:
    print(f"A meta foi atingida com {jeans_vendidos} jeans vendidos.")
else:
    estoque_atual = estoque - jeans_vendidos
    em_estoque = estoque_atual != 0
    if estoque != 0:
        print(f"Jeans em estoque: {estoque_atual} para vender ainda.")
