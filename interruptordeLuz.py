"""Python Basics
    nível = Easy
"""

print('\t*' * 10)
print('\t\t    Interruptor de luz')
print('\t*' * 10)

eh_dia = input("É dia? [S/N]: ").upper()
horario = 0
luz = 0
if eh_dia == 'S' or eh_dia == 'SIM':
    luz = 'desligada'
    horario = 'dia'
elif eh_dia == 'N' or eh_dia == 'NAO' or eh_dia == "NÃO":
    luz = 'ligada'
    horario = 'noite'

print('\tFoi constantado que: ')
print('\t.' * 3)
print(f"\t- É {horario}\n\t- A luz está {luz}")
