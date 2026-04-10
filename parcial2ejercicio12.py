texto = "ING. Marjhory Odalis Alvarez Cortez.txt"
sin_sufijo = texto.removesuffix(".txt")
limpio = sin_sufijo.removeprefix("ING. ")
final = limpio.lower()
print("Texto final: ", final)