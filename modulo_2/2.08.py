print("insere um ano:")
ano = int(input())

if(ano % 4 == 0 and ano % 100 > 0 or ano % 400 == 0):
    print("ano bissexto")
else:
    print("ano normal")

# github

# ano = int(input("Insira um ano: "))

# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print("Ano bissexto")
# else:
#     print("Ano normal")
