'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input("Digite uma letra: ")

vogais = 'aeiou'

if letra in vogais or letra in vogais.upper():
    print(f"A letra {letra} é uma VOGAL!")
else:
    print(f"A letra {letra} é uma CONSOANTE")
