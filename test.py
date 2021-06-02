

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

#função deposito
def deposita(conta, valor):
    conta["saldo"] += valor

#função sacar dinheiro
def saca(conta, valor):
    conta["saldo"] -= valor

#função extrato
def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

