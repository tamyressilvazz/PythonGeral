"""
. Crie uma tupla com números de 0 a 9 (em qualquer ordem) e tente:
a. Alterar o valor do 3º elemento da tupla para o valor 10
b. Verificar o índice (posição) do valor 5 na tupla
"""

tupla_n = (0,1,2,3,4,5,6,7,8,9)
# transforma a tupla numa lista para fazer a troca
list_n = list(tupla_n)

#troca o elemento por outro
list_n[2] = 10

#transforma de volta em tupla
back_tupla = tuple(list_n)

#obtendo a posição do valor 5
print(back_tupla.index(5))




