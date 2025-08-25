"""
Adicionar novo par chave-valor : adicione um novo par chave-valor,  
    'profession': 'Doctor', ao dicionário e imprima o dicionário atualizado.
Modificar valor : altera o valor da age-chave para 40 no dicionário e imprime o dicionário atualizado.
Chave de acesso: imprima o valor associado à city-chave.
"""
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

#adicionando um par de chave e valor no dicionário
my_dict.update({'profession': 'Doctor'})
#print(my_dict)

#alterando o valor da chave 'age'
my_dict['age'] = 40
#print(my_dict)

#valor da chave city
#print(my_dict.get('city'))

"""
Remover par chave-valor : Remove o profession par chave-valor do dicionário.
Obter itens (pares chave-valor): imprimir todos os pares chave-valor (itens) no dicionário.
Verifique se a chave existe no dicionário
"""
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

#removendo o par chave e valor profession
del my_dict['profession']

#todos os pares chave-valor do dicionário
#print(my_dict)

#verifica se a chave age está dentro de dicionário
if 'age' in my_dict:
    res = True
else: res = False
#print(f'age in dict? {res}')

"""
converter duas listas Python em um dicionário onde os elementos da primeira lista 
se tornam chaves e os elementos da segunda lista se tornam valores.
"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#iterando para tornar os elementos das listas em par-valor
my_dict = {key: value for key, value in zip(keys, values)}
#print(my_dict)

"""
Limpa todos os pares chave-valor de um dicionário fornecido e imprime-o.
"""
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

#limpa todos os elementos do dicionário
my_dict.clear()
#print(my_dict)


"""
Escreva um código para mesclar dois dicionários em um novo dicionário e imprimi-lo.
"""
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

new_dict = {**dict1, **dict2} # tambem pode ser feito c dict1.update(dict2)
#print(new_dict)

"""
Dada uma string, crie um dicionário onde as chaves são caracteres e os valores são suas frequências na string.
Frequências para 'Jessa': {'J': 1, 'e': 1, 's': 2, 'a': 1}
"""
string1 = 'Jessa'
count_str_1 = string1.count(string1[0])
count_str_2 = string1.count(string1[1])
count_str_3 = string1.count(string1[2])
count_str_4 = string1.count(string1[3])
count_str_5 = string1.count(string1[-1])

#transformo a string em uma lista dos caracteres
str_name = list(string1)
#pego os count dos caracteres da string
str_list = [count_str_1, count_str_2, count_str_3, count_str_4, count_str_5]

#itero para transformar as duas listas com zip em um dict chave-valor
my_dict = {key: value for key, value in zip(str_name, str_list)}

print(f'Frequências para {string1}: {my_dict}')

"""
Dado um dicionário aninhado {'person': {'name': 'Alice', 'age': 30}}, imprima a idade de Alice.
"""

