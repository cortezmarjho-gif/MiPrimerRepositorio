pos = 0
neg = 0

num = int(input("Escribe un número (0 para salir): "))

while num != 0:

    if num > 0:
        pos = pos + 1
    else:
        neg = neg + 1

    num = int(input("Escribe otro número (0 para salir): "))

print("Resultado:")

lista = [pos, neg]

for i in range(2):
    if i == 0:
        print("Positivos:", lista[i])
    else:
        print("Negativos:", lista[i])