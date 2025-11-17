i = 0
soma = 0

print("insere um número:")
digitado = input()

while digitado != "sair":
    soma = soma + int(digitado)
    i = i+1

    print("insere um número:")
    digitado = input()

print(f"foram digitados {i} número(s) e a soma é {soma}")

#github

# i = 0
# soma = 0

# while True:
#     digitado = input("insere um número: ")
#     if digitado == "sair":
#         break
#     soma += int(digitado)
#     i += 1

# print(f"foram digitados {i} número(s) e a soma é {soma}")
