usuario_correcto = "mar"
contraseña_correcta = "1010"

usuario = input("Ingrese su usuario:   ")
contraseña = input("Ingrese su contraseña:   ")

if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Acceso permitido")    

else:
    print("Acceso denegado")