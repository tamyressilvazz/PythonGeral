"""
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
def pede_valor(num):
    num = int(input("Digite um número: "))
    
    return num

def verifica_p_n():
    valor = pede_valor()
    
    if valor < 0:
        res = "Negativo"
    elif valor == 0:
        res = "Zero"
    else: res = "Positivo"
    return res

#verifica_p_n(5)

"""
Faça um programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

def pede_usuario(letra: str):
    letra = input("Informe o sexo (F-Feminino, M-Masculino): ").lower()
    return letra

def verifica_sexo():
    sexo = pede_usuario('F')

    if sexo == 'F':
        res = "Feminino"
    elif sexo == 'M':
        res = "Masculino"
    else:
        res = "Inválido"
    print(f"O valor é {res}")

#verifica_sexo()

"""
Faça um programa que verifique se uma letra digitada é vogal ou consoante.
"""
def vogal_cons(letra):
    vogais = ['a','e','i','o','u']

    consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']

    letra = input("Digite uma letra: ").lower()

    if letra.isalpha: 
        for i in vogais:
            if letra == i:
                res = "Vogal"
        for i in consoantes:
            if letra == i:
                res = "Consoante"
        
    else:
        res = "Inválido"


#print(f"A letra {letra} é uma {res}")

"""
Faça um programa que leia três números e mostre o maior deles:
"""

num_1 = 2
num_2 = 4
num_3 = 8

list_num = [num_1, num_2, num_3]

maior = max(list_num)
menor = min(list_num)

#print(f"O maior número é {maior}, o menor número é {menor}")

"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato:
"""

produto_1 = 13.76
produto_2 = 15.90
produto_3 = 18.47

list_prod = [produto_1, produto_2, produto_3]

mais_barato = min(list_prod)

if produto_1 == list_prod[0]:
    print(f"O produto mais barato é o Produto 01")
elif produto_2 == list_prod[1]:
    print("O produto mais barato é o Produto 02")
else:
    print("O produto mais barato é o Produto 03")

"""
Faça um programa que leia três números e mostre-os em ordem decrescente:
"""
def ordena_cres(num_1, num_2, num_3)->list:
    """num_1 = 2
    num_2 = 4
    num_3 = 8"""

    list_num = [num_1, num_2, num_3]

    crescente = sorted(list_num, reverse=False)
    for i in crescente:
        print(i)

#ordena_cres(2,7,1)

"""
Faça um programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
