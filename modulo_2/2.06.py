print("insere 3 lados:")
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

if(not (lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2)):
    print("não é um triângulo!")
elif(lado1 == lado2 == lado3):
    print("equilatero")
elif(lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
    print("isósceles")
else:
    print("escaleno")


# copilot

# def tipo_triangulo(lado1, lado2, lado3):
#     lados = sorted([lado1, lado2, lado3])
#     if lados[0] + lados[1] <= lados[2]:
#         return "não é um triângulo!"
#     if lados[0] == lados[1] == lados[2]:
#         return "equilatero"
#     if lados[0] == lados[1] or lados[1] == lados[2]:
#         return "isósceles"
#     return "escaleno"

# print("insere 3 lados:")
# try:
#     lados = [float(input()) for _ in range(3)]
#     print(tipo_triangulo(*lados))
# except ValueError:
#     print("Entrada inválida.")
