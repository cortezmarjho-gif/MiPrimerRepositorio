Algoritmo Nota_estudiante
	
	Definir nota Como Entero
	
	Escribir "Ingrese la nota 0 a 10"
	Leer nota 
	
	Si nota <=4 Entonces
		Escribir "Reprobado"
	SiNo
		si nota = 5 Entonces
			Escribir "Recuperacion"
		SiNo
			si nota <= 10 Entonces
				Escribir "Aprobado"
			sino
				si nota > 10 entonces
					Escribir "Nota no valida"
				FinSi
			FinSi
		Fin Si
	FinSi
FinAlgoritmo 

	
