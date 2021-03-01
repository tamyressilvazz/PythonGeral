import turtle           # funções necessárias para criar um objeto do tipo turtle

print("------EXEMPLO DE CORES-------")
print("red, brown, black...")
tess = turtle.Turtle()                              # Cria tess
tess.color(input("Cor da tartaruga Tess? "))        # cor da tartaruga

print("-----EXEMPLO DE CORES------")
print("blue, lightblue, green, lightgreen")
wn = turtle.Screen()                            #mostra tess na tela gráfica
wn.bgcolor(input("Cor do fundo: "))         # define a cor de fundo da janela

print("------EXEMPLO DE ESPESSURA-------")
print("\t2, 3, 5...")
tess.pensize(int(input("Espessura da caneta: ")))    # define a espessura da caneta

alex = turtle.Turtle()           # cria alex

tess.forward(80)                 # tess desenha um triângulo equilátero
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete o triângulo

tess.right(180)                  # tess muda de direção
tess.forward(80)                 # tess se move para longe da origem

alex.forward(50)                 # alex desenha um quadrado
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
