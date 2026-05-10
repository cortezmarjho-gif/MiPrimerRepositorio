def mayor(arreglo):

    numMayor = arreglo[0]

    for i in arreglo:
        if i > numMayor:
            numMayor = i

    return numMayor


numeros = []

for x in range(8):
    n = int(input("Ingrese un número: "))
    numeros.append(n)

print("El número mayor es:", mayor(numeros))