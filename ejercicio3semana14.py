def sacar_promedio(notas):

    suma = 0

    for nota in notas:
        suma = suma + nota

    promedio = suma / len(notas)

    return promedio


arreglo = []

for i in range(5):
    n = float(input("Ingrese una nota: "))
    arreglo.append(n)

prom = sacar_promedio(arreglo)

print("El promedio es:", prom)

if prom >= 6:
    print("El grupo aprobó")
else:
    print("El grupo reprobó")