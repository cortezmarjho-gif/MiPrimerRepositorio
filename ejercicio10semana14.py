def ordenar_numeros(numeros):

    for i in range(6):

        for j in range(5):

            if numeros[j] > numeros[j + 1]:

                temp = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = temp

    return numeros


arreglo = []

for x in range(6):
    n = int(input("Ingrese un número: "))
    arreglo.append(n)

print("Números ordenados:")
print(ordenar_numeros(arreglo))