def suma_pares(arreglo):

    suma = 0

    for num in arreglo:
        if num % 2 == 0:
            suma = suma + num

    return suma


numeros = []

for i in range(6):
    n = int(input("Ingrese un número: "))
    numeros.append(n)

print("La suma de los números pares es:", suma_pares(numeros))