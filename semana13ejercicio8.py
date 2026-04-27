num = int(input("Pon un número (0 para salir): "))

while num != 0:

    for i in range(1, num + 1):

        if i % 2 != 0:
            print("*" * i)

    num = int(input("Pon otro número (0 para salir): "))