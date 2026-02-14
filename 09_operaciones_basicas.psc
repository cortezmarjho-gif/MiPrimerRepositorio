Algoritmo operaciones_basicas
    Definir a, b, suma, resta, multi, div Como Real
    
    Escribir "Ingrese dos numeros:"
    Leer a, b
    
    suma <- a + b
    resta <- a - b
    multi <- a * b
    
    Escribir "Suma: ", suma
    Escribir "Resta: ", resta
    Escribir "Multiplicacion: ", multi
    
    Si b <> 0 Entonces
        div <- a / b
        Escribir "Division: ", div
    Sino
        Escribir "Division: No se puede dividir entre cero"
    FinSi
	
FinAlgoritmo
