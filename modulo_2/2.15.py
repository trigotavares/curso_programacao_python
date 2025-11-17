letras = 0
espacos = 0
digitos = 0

print("Insere uma string:")
string = input()

for char in string:
    if char == ' ':
        espacos += 1
        continue

    if(char >= '0' and char <= '9'):
        digitos += 1
        continue

    letras += 1

print(f"a tua frase tem {espacos} espaço(s), {digitos} número(s) e {letras} letra(s)")

# # Versão otimizada usando métodos de string
# letras = sum(char.isalpha() for char in string)
# espacos = string.count(' ')
# digitos = sum(char.isdigit() for char in string)

# print(f"a tua frase tem {espacos} espaço(s), {digitos} número(s) e {letras} letra(s)")
