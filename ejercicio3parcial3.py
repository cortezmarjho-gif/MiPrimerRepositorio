temperaturas = []

for i in range(5):

    temp = int(input("Ingrese una temperatura: "))
    temperaturas.append(temp)

for t in temperaturas:

    match t:

        case 0:
            print("Alerta: Punto de Congelación")

        case 100:
            print("Alerta: Punto de Ebullición")

        case _:

            if t >= 10 and t <= 30:
                print("Estado Estable")

            else:
                print("Estado Crítico")