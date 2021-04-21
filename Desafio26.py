print("------DESAFIO 26------")
print("----Primeira e última ocorrência de uma string----")

texto = input("Digite uma frase: ").upper()

quantia = texto.count('A')
posicao_first = texto.find('A')
posicao_Last = texto.rfind('A')

print(f"\tA letra A apareceu {quantia} vezes na frase.")
print(f"\tA primeira letra A apareceu na posição {posicao_first}")
print(f"\tA última letra A apareceu na posição {posicao_Last}")