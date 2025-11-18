listaCompras = ["bananas", "peitos de frango", "liquido da loiça", "fósforos"]

# Adicionar um item

listaCompras = listaCompras + ["lata de atum"]

print(listaCompras)

# Remover um item

listaCompras.remove("peitos de frango")

print(listaCompras)

# Verificar se um item está na lista

itemAEncontrar = "peitos de frango"
encontrado = False

for item in listaCompras:
    if(item == itemAEncontrar):
        encontrado = True
        break
    
print(f"item {itemAEncontrar} {"encontrado" if encontrado else "não encontrado"}")

# Ordenar alfabeticamente

listaCompras.sort()
print(listaCompras)

