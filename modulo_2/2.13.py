print("insere um nº para ser calculado o seu fatorial:")
n = int(input())
fatorial = 1

for i in range(0,n):
    fatorial = fatorial * (n - i)

print(fatorial)

#github
# def calcular_fatorial(n):
#     fatorial = 1
#     for i in range(2, n + 1):
#         fatorial *= i
#     return fatorial

# n = int(input("Insira um número para calcular o seu fatorial: "))
# print(calcular_fatorial(n))