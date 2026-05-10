def mayores_edad(edades):

    contador = 0

    for edad in edades:
        if edad >= 18:
            contador += 1

    return contador


arreglo = []

for i in range(6):
    e = int(input("Ingrese una edad: "))
    arreglo.append(e)

print("Cantidad de mayores de edad:", mayores_edad(arreglo))