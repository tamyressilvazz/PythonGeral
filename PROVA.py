import sys

nota1 = [30, 65, 64, 83, 46, 44, 57, 27, 24, 84, 93, 35, 90, 83, 31, 73, 55, 96, 82, 88, 66, 25, 47, 77, 51, 78, 49]
nota2 = [96, 54, 96, 62, 63, 62, 71, 78, 75, 27, 85, 81, 42, 98, 89, 69, 93, 95, 52, 62, 31, 97, 21, 48, 66, 48, 24]
notas = nota1 + nota2

notas.sort(reverse=True)
print(f"Cinco melhores pontuações: {notas[0:5]}")

last_nota = list()
last_nota.append(int(input("Qual a pontuação do último candidato? ")))
new_list = notas + last_nota

maiores = len(list(filter(lambda i: i > new_list[54], new_list)))
iguais = len(list(filter(lambda i: i == new_list[54], new_list)))
print(f'\tA quantidade de notas maiores que o último são: {maiores}')
print(f'\tA quantidade de notas iguais que o último são: {iguais}')
