import random

def mayores_50(arreglo):

    contador = 0

    for num in arreglo:
        if num > 50:
            contador = contador + 1

    return contador


numeros = []

for i in range(10):
    n = random.randint(1, 100)
    numeros.append(n)

print("Números generados:")
print(numeros)

print("Cantidad mayores a 50:", mayores_50(numeros))