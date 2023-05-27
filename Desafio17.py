from math import sqrt
print("------DESAFIO 17------")
print("----Cateto e Hipotenusa----")

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento de cateto adjacente: "))

hipotenusa = sqrt(co ** 2 + ca ** 2)

print("\tHipotenusa:")
print("\tA hipotenusa vai medir {:.2f}".format(hipotenusa))