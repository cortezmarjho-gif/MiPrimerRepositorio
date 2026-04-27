n = int(input("Pon un número (0 para salir): "))

while n != 0:

    print("Pares con for:")
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)

    print("Pares con while:")
    i = 1
    while i <= n:
        if i % 2 == 0:
            print(i)
        i = i + 1

    n = int(input("Pon otro número (0 para salir): "))