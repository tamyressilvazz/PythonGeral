'''Python Basics
    nível = Medium
'''
import time
print('\t*' * 10)
print('\t\t  SISTEMA DE CONVERSÃO')
print('\t*' * 10)
milhas = float(input("Quantas milhas? "))
kilometros = milhas * 1.609344
print("\t\tCONVERTENDO . . .")
time.sleep(3)
print(f"\t\t {milhas} milhas -----> {kilometros} Km ")