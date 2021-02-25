'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input("Digite uma letra: ") #guarda a letra digitada em letra

vogais = 'aeiou'                    #string com as vogais

if letra in vogais or letra in vogais.upper():      #verifica se a letra está em vogais minuscula OU vogais maiusculas
    print(f"A letra {letra} é uma VOGAL!")         
else:                                               #se não for uma vogal, consequentemente é uma consoante
    print(f"A letra {letra} é uma CONSOANTE")
