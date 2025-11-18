mat = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

# Soma de cada linha

for linha in mat:
    print(sum(linha))

# Soma de cada coluna

numLinhas = len(mat)
numColunas = len(mat[0])

for i in range(0,numColunas):
    soma = 0
    for linha in mat:
        soma += linha[i]
    print(soma)