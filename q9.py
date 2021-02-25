'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-
Segunda, etc.), se digitar outro valor deve aparecer valor inválido
'''

print("----------Exemplo de Entrada------------")
print("1 - Domingo\n2 - Segunda\nE assim sucessivamente") #Demonstrando com Exemplo
dia_Semana = input("Digite o número que represente o dia da semana: ") #Solicitando ao usuário o dia

dia = ['1', '2', '3', '4', '5', '6', '7']

if dia_Semana in dia:
    if dia_Semana == dia[0]:        #se o dia digitado for igual ao item de índice 0 da lista dia
        print(f"{dia_Semana} - DOMINGO")
    elif dia_Semana == dia[1]:      #se o dia digitado for igual ao item de índice 1 da lista dia
        print(f"{dia_Semana} - SEGUNDA")
    elif dia_Semana == dia[2]:      #se o dia digitado for igual ao item de índice 2 da lista dia
        print(f"{dia_Semana} - TERÇA")
    elif dia_Semana == dia[3]:      #se o dia digitado for igual ao item de índice 3 da lista dia
        print(f"{dia_Semana} - QUARTA")
    elif dia_Semana == dia[4]:      #se o dia digitado for igual ao item de índice 4 da lista dia
        print(f"{dia_Semana} - QUINTA")
    elif dia_Semana == dia[5]:      #se o dia digitado for igual ao item de índice 5 da lista dia
        print(f"{dia_Semana} - SEXTA")
    if dia_Semana == dia[6]:        #se o dia digitado for igual ao item de índice 6 da lista dia
        print(f"{dia_Semana} - SÁBADO")
else:   #SENÃO o dia digitado será inválido
    print(f"{dia_Semana} é um dia inválido!!!")