""" verificaremos as respostas da pesquisa do usuário
    com relação à frequência e intensidade da atividade,
    rotular e exibir os resultados.
"""

frequencia = int(input("Quantas vezes você faz exercícios físicos durante a semana?  "))
intensidade = input("Entre 'Baixo' e 'Alto', como se encontra sua intensidade de atividades físicas? ").upper()

if frequencia >= 3:
    print(f"Indivíduo altamente ativo.")
elif frequencia < 3:
    print("Frequência baixa")
    if frequencia == 0:
        print("Você está sedentário")
if intensidade == 'ALTO':
    print("Você tem disposição para esportes de alta intensidade!")
