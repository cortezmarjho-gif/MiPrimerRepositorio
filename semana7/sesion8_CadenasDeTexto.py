# las comillas triples son las que se encargan de hacer
#Cadenas de texto largas sin modificacion el formato"
#2 comillas es para texto corto
#3comillas es para texto largo

cancion= """Te regalo mis piernas, recuesta tu cabeza en ellas.
Te regalo mis fuerzas, usa las que quieras.
Te regalo las piezas que a mi alma conforman, que nunca nada te haga falta a ti."""

##print(cancion)

##computadora -> que variable queres imprimir
## como sabe, por el metodo "print"
# print() -> es la función que se encarga de imprimir pantalla
# void -> no devuelve nada
# objeto -> devuelve un tipo de dato

# realizar una wiki, tambien se puede ver dando doble clic
# en el documeto y se les despelga el editor de texto
## esa canción a mayusculas
## mutabilidad -> siempre debemos evitar transformar objeto original
## clases -> estereotipo ( defini: como un  molde)
## estan formadas por propiedades ->
## music es un espacio de memoria para string
## se va a llenar con el contenido de music


cancion_Mayusculas = cancion.upper()
##print(cancion_Mayusculas)

## convertir en minisculas
## string .lower

cancion_minuscula = cancion.lower()
print(cancion_minuscula)

## tiene que ingresar 100 nombres en mayuscula
