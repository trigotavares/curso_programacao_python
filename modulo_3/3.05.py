mat = [
    [21, 41, 6, 11],
    [17, 3, 50, 53],
    [71, 82, 9, 2],
    [16, 4, 42, 51]
]

numLinhas = len(mat)
numColunas = len(mat[0])

valorMax = 0
linhaMax = -1
colunaMax = -1

for coluna in range(0,numColunas):
    for linha in range(0,numLinhas):
        if(mat[linha][coluna] > valorMax):
            valorMax = mat[linha][coluna]
            linhaMax = linha
            colunaMax = coluna

print(f"O valor máximo é {valorMax}, na coluna {colunaMax} da linha {linhaMax}")