saldo = 1500.25
digitado = 0


while digitado != "n":
    print("insere o valor a levantar (€):")
    digitado = input()

    saldo = saldo - float(digitado)

    print("deseja continuar?")
    digitado = input()

print(f"saldo disponível: {saldo}€")

#copilot

# saldo = 1500.25

# while True:
#     valor = input("Insere o valor a levantar (€): ")
#     try:
#         valor = float(valor)
#     except ValueError:
#         print("Valor inválido. Tente novamente.")
#         continue

#     if valor > saldo:
#         print("Saldo insuficiente.")
#         continue

#     saldo -= valor

#     continuar = input("Deseja continuar? (s/n): ").lower()
#     if continuar == "n":
#         break

# print(f"Saldo disponível: {saldo:.2f}€")