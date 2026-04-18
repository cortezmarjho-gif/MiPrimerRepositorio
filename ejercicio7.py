monto = float (input("Ingrese el monto de la compra: "))    

if monto > 100:
    descuento = monto * 0.20

elif monto > 50:
    descuento = monto * 0.10

else:
    descuento = 0   

total = monto - descuento
print("El descuento aplicado es:", descuento)
print("El monto total a pagar es:", total)
