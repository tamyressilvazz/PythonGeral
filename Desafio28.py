import random
from time import sleep

print("------DESAFIO 28------")
print("----Jogo da advinhação v.1.0---")

numero = random.randrange(0, 6)
frase = "\t\t\tVou pensar em um número entre 0 e 5. Tente adivinhar se for capaz..."
tam = len(frase)
print('.*' * tam)
print(frase)
print('.*' * tam)
descubra = int(input("Em que número pensei? "))
print("P R O C E S S A N D O . . .")
sleep(2)
if descubra == numero:
    print(f"VOCÊ VENCEU DESSA VEZ! Eu pensei no número {numero}.")
elif descubra != numero and descubra >= 0 and descubra < 6:
    print(f"GANHEI! Eu pensei no número {numero} e não em {descubra}!")
else:
    print(f"O número digitado é inválido")

