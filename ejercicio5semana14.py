def numeros_positivos(numeros):

    positivos = []

    for num in numeros:
        if num > 0:
            positivos.append(num)

    return positivos


arreglo = []

for i in range(6):
    n = int(input("Ingrese un número: "))
    arreglo.append(n)

resultado = numeros_positivos(arreglo)

print("Números positivos:")
print(resultado)