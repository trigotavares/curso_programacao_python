lista = [5, 7, 12, 56, 100, 45, 3, 6]

print(f"maior número: {max(lista)} - menor número: {min(lista)}")

soma = sum(lista)
media = soma / len(lista)

print(f"soma: {soma} - média: {media}")

for i in lista:
    if(i > media):
        print(i)