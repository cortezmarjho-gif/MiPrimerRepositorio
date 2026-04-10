texto = "python2026"
alfanumerico = texto.isalnum()

if alfanumerico:
    minuscula = texto.lower()
    texto_final = minuscula.replace("2026", "")
    print("Texto final: ", texto_final)
else:
    print("El texto no es alfanumérico.")
      