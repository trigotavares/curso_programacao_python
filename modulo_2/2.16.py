turma = [12, 15, 9, 17, 14, 10]

soma = 0
total = 0
for nota in turma:
    soma += nota
    total += 1

media = soma / total

acimaMedia = 0
for nota in turma:
    if(nota > media):
        acimaMedia += 1
    
abaixoMedia = total - acimaMedia

print(f"A média foi {media}, houveram {acimaMedia} acima da média e {abaixoMedia} abaixo da média")

# OTIMIZADO:
# turma = [12, 15, 9, 17, 14, 10]

# media = sum(turma) / len(turma)
# acimaMedia = sum(nota > media for nota in turma)
# abaixoMedia = len(turma) - acimaMedia

# print(f"A média foi {media}, houveram {acimaMedia} acima da média e {abaixoMedia} abaixo da média")
