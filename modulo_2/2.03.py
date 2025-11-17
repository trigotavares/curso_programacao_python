peso = 85
altura = 1.79

imc = peso/(altura ** 2)

print(f"imc: {imc}")

if imc < 18.5:
    print("Magreza")
elif imc < 24.9:
    print("Normal")
elif imc < 29.9:
    print("Obesidade grau I")
elif imc < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")

# copilot
# def calcula_imc(peso, altura):
#     imc = peso / (altura ** 2)
#     print(f"imc: {imc:.2f}")
#     if imc < 18.5:
#         print("Magreza")
#     elif imc < 24.9:
#         print("Normal")
#     elif imc < 29.9:
#         print("Obesidade grau I")
#     elif imc < 39.9:
#         print("Obesidade grau II")
#     else:
#         print("Obesidade grau III")

# peso = 85
# altura = 1.79
# calcula_imc(peso, altura)