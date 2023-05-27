print("==========Desafio 04==========")
print("--------TIPOS PRIMITIVO DE DADOS--------")
algo = input("Digite algo: ")

print(f"O tipo primitivo desse valor é {type(algo)}")
print(f"Só tem espaços? {algo.isspace()}")
print(f"É um número? {algo.isnumeric()}")
print(f"É alfabético? {algo.isalpha()}")
print(f"É alfanúmerico? {algo.isalnum()}")
print(f"É maiúscula? {algo.isupper()}")
print(f"É minúscula? {algo.islower()}")
print(f"É capitalizada? {algo.istitle()}")

print("============FIM============")