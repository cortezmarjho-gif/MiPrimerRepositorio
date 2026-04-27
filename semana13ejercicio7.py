notas = []

nota = float(input("Pon una nota (-1 para salir): "))

while nota != -1:

    if nota >= 0 and nota <= 10:
        notas.append(nota)
    else:
        print("Nota mala")

    nota = float(input("Pon otra nota (-1 para salir): "))

suma = 0

for i in range(len(notas)):
    suma = suma + notas[i]

if len(notas) > 0:
    prom = suma / len(notas)
    print("Promedio:", prom)
else:
    print("No pusiste notas buenas")