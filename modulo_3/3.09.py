string = "aaaabbbccaadd"
removidos = 0

semDuplicados = ""

for index in range(0, len(string)):
    charAtual = string[index]
    if(charAtual not in semDuplicados):
        semDuplicados += charAtual

print(semDuplicados)