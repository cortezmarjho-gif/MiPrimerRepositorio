suma = 0
nums = []

while suma <= 100:

    n = int(input("Escribe un número: "))

    if n >= 0:
        suma = suma + n
        nums.append(n)
    else:
        print("No se puede negativo")

print("Ya pasó de 100")

print("Números válidos:")

for i in range(len(nums)):
    print(nums[i])