Algoritmo bucle
	Definir contador Como Entero
	//contador i i++ i--
	Escribir " numero del 0 al 100"
	leer numeroEntrada
	contador = 1
	resultado = 0
	anterior = 0

	Mientras contador < numeroEntrada
		anterior = contador
		contador = contador + 1
		resultado = contador + anterior 
		Escribir "resultado es ", contador , " + " , anterior, " = " , resultado
		
	FinMientras
	
	
	
	Escribir "password"
	leer pass
	
	Mientras pass <> "nombre de ella + fecha especial"
		Escribir "romper bucle infinito 1 si 2 no"
		leer respuesta
		si respuesta == "no"
		FinSi
		si respuesta == "si"
			pass = "nombre de ella + fecha especial"
		FinSi
	FinMientras	
	
	Escribir "Final"
FinAlgoritmo
