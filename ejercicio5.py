num1 = float (input("Ingrese el primer número: "))
num2 = float (input("Ingrese el segundo número: "))     
operacion = input("Ingrese la operación a realizar (+, -, *, /): ") 

if operacion == "+":
    print("El resultado de la suma es:", num1 + num2)

elif operacion == "-":
    print("El resultado de la resta es:", num1 - num2)

elif operacion == "*":
    print("El resultado de la multiplicación es:", num1 * num2) 

elif operacion == "/":
    if num2 != 0:
        print("El resultado de la división es:", num1 / num2)
    else:
        print("No se puede dividir entre cero.")

else:
    print("Operación inválida.")