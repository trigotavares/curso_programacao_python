print("Insere o valor de uma compra:")
valor_compra = float(input())

if(valor_compra < 100):
    print(f"Sem desconto. Vais pagar {valor_compra}")
elif(valor_compra < 500):
    print(f"10% de desconto. Vais pagar {valor_compra - valor_compra * 0.1}")
else:
    print(f"20% de desconto. Vais pagar {valor_compra - valor_compra * 0.2}")

#copilot

# valor_compra = float(input("Insere o valor de uma compra: "))

# if valor_compra < 100:
#     desconto = 0
# elif valor_compra < 500:
#     desconto = 0.1
# else:
#     desconto = 0.2

# valor_final = valor_compra * (1 - desconto)

# if desconto == 0:
#     print(f"Sem desconto. Vais pagar {valor_final}")
# else:
#     print(f"{int(desconto*100)}% de desconto. Vais pagar {valor_final}")