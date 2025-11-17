print("insere a hora atual (0-23):")
hora_atual = int(input())

if hora_atual >= 9 and hora_atual <= 18:
    print("Loja aberta")
else:
    print("Loja fechada")

#copilot

# hora_atual = int(input("Insira a hora atual (0-23): "))

# print("Loja aberta" if 9 <= hora_atual <= 18 else "Loja fechada")
