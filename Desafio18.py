import math
print("------DESAFIO 18------")
print("----Seno, Cosseno, Tangente----")

angulo = float(input("Digite o ângulo que você deseja: "))
angulo = math.radians(angulo)

'''Seno do ângulo'''
seno = math.sin(angulo)     #Converte de graus para radianos

'''Cosseno'''
cosseno = math.cos(angulo)

'''Tangente'''
tangente = math.tan(angulo)

print("\tDADOS DO ÂNGULO:")
print("\tO ângulo de {:.2f} tem o SENO de {:.2f}".format(angulo, seno))
print("\tO ângulo de {:.2f} tem o COSSENO de {:.2f}".format(angulo, cosseno))
print("\tO ângulo de {:.2f} tem o TANGENTE de {:.2f}".format(angulo, tangente))
