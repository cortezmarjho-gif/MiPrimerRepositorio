from decimal import Decimal

total = Decimal("0")

while True:

    try:
        
        precio = Decimal(input("Ingrese el precio del producto: "))

        if precio == 0:
            break

        total += precio

    except:
        print("Dato inválido")

print("Total acumulado:", total)