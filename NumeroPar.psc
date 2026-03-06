Algoritmo NumeroPar
		
		Definir num Como Entero
		Definir continuar Como Entero
		
		continuar <- 1 
	    Mientras 	continuar = 1 Hacer
		Escribir "Ingrese un número:"
			Leer num
			
			Si (num % 2 = 0 Y num <> 0) Entonces
				Escribir "El número es PAR"
			SiNo
				Escribir "El número es IMPAR"
			FinSi
			
			Escribir "¿Desea continuar? (1 = Sí / 0 = No):"
			Leer continuar
		
		Fin Mientras
FinAlgoritmo
