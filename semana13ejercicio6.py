n = int(input("Pon un número (0 para salir): "))

while n != 0:

    print("Números primos:")

    for num in range(1, n + 1):

        if num > 1:
            cont = 0

            for i in range(1, num + 1):
                if num % i == 0:
                    cont = cont + 1

            if cont == 2:
                print(num)

    n = int(input("Pon otro número (0 para salir): "))