texto = "CANTANDO"
minuscula = texto.lower()
texto_sin_prefijo = minuscula.removesuffix("ando")
t = texto_sin_prefijo.find("t")
print("Texto final: ", texto_sin_prefijo)
print("Indice de la letra 't': ", t)
