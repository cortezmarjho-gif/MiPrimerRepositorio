def contar_pares_impares(lista):
    pares = 0
    impares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares


# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares, impares = contar_pares_impares(numeros)

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)