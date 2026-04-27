num = int(input("Pon un número (-1 para salir): "))

while num != -1:

    print("Tabla:")

    for i in range(1, 11):
        r = num * i

        if r > 20:
            print(num, "x", i, "=", r)

    num = int(input("Pon otro número (-1 para salir): "))
