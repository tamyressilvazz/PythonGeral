#Descriptografando
cifra = input('Digite a frase criptografada: ')
texto = ''
for char in cifra:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    texto += chr(code)

print(texto)