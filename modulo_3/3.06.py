x = int(input("insira o x:"))
y = int(input("insira o y:"))

coordenadas = (x, y)

if(coordenadas[0] > 0):
    if(coordenadas[1] > 0):
        print("I")
    elif(coordenadas[1] < 0):
        print("IV")
    else:
        print("Encontra-se no eixo de Y")
elif(coordenadas[0] < 0):
    if(coordenadas[1] > 0):
        print("II")
    elif(coordenadas[1] < 0):
        print("III")
    else:
        print("Encontra-se no eixo de Y")
else:
    if(coordenadas[1] == 0):
        print("Encontra-se no eixo de X e Y")
    else:
        print("Encontra-se no eixo de X")
