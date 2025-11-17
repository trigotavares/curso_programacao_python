listaFrases = [
    "Olá sou um texugo.",
    "Então como andas?",
    "",
    "Como o macaco gosta da banana...",
]

palavraUtilizador = input("Insira a palavra a procurar:")

for frase in listaFrases:
    if(frase == ''):
        continue

    palavras = frase.split()
    for palavra in palavras:
        if(palavra == palavraUtilizador):
            print(f"Palavra encontrada na frase '{frase}'!")
            break

# Otimização: Remover duplicação, usar list comprehension e funções integradas

# listaFrases = [
#     "Olá sou um texugo.",
#     "Então como andas?",
#     "",
#     "Como o macaco gosta da banana...",
# ]

# palavraUtilizador = input("Insira a palavra a procurar:")

# for frase in filter(None, listaFrases):
#     if palavraUtilizador in frase.split():
#         print(f"Palavra encontrada na frase '{frase}'!")
