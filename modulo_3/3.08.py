vogais = 0
consoantes = 0
espacos = 0
digitos = 0

print("Insere uma string:")
string = input()

vogais = sum(char.lower() in ["a","e","i","o","u"] for char in string)
consoantes = sum((char.isalpha() and char.lower() not in ["a","e","i","o","u"]) for char in string)
espacos = string.count(' ')
digitos = sum(char.isdigit() for char in string)

print(f"a tua frase tem {espacos} espaço(s), {digitos} número(s), {vogais} vogal(is) e {consoantes} consoante(s)")