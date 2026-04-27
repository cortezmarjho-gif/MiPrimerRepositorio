clave = "1234"
fallos = 0

contra = input("Pon la contraseña: ")

while contra != clave:

    if contra != clave:
        print("Contraseña mala")
        fallos = fallos + 1

    contra = input("Pon otra vez la contraseña: ")

print("Entraste")

print("Intentos fallidos:")

for i in range(1, fallos + 1):
    print("Fallo", i)