for i in range(1,51):

    if i % 5 == 0:
        continue

    if i == 42:
        print("Proceso interrumpido")
        break

    print("Procesando registro ID", i)