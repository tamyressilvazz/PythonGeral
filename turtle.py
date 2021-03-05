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
for aColor in ["yellow", "red", "purple", "blue"]:  # repita 4 vezes
    alex.forward(50)
    alex.left(90)

for i in [0,1,2,3]:      # repita 4 vezes
    tess.forward(50)
    tess.left(90)               # tess se move para longe da origem




wn.exitonclick()
