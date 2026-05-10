def nombres_largos(nombres):

    print("Nombres con más de 5 letras:")

    for nombre in nombres:
        if len(nombre) > 5:
            print(nombre)


arreglo = []

for i in range(10):
    nom = input("Ingrese un nombre: ")
    arreglo.append(nom)

nombres_largos(arreglo)