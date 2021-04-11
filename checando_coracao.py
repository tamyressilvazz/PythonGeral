"""usaremos comparações para verificar
    se a frequência cardíaca está muito baixa ou muito alta
    e dizer ao paciente se ele deve se preocupar com sua saúde.
"""
import emoji
frequencia_cardio = int(input("Em quanto sua frequência cardíaca está? "))

if frequencia_cardio < 60:
    print(emoji.emojize(f":ambulance: {frequencia_cardio} é uma frequência muito baixa :ambulance:"))
elif frequencia_cardio > 100:
    print(emoji.emojize(f":ambulance: {frequencia_cardio} é uma frequência muito alta! :ambulance:"))
elif frequencia_cardio >= 60:
    print(f"{frequencia_cardio} é uma frequência normal.")
    if frequencia_cardio == 100:
        print(emoji.emojize(f":warning: Porém, tenha Cuidado :warning:"))