# las variables sirven para guardar datos en memoria.
# asignamos una variable con el operador =

my_name = "laura"
print(my_name)

age = 32
(print(age))

age = 39

(print(age))  #las variables se pueden reasignar

#tipado dinamico (python): el tipo de dato se determina en tiempo de ejecucion, no tenemos que declararlo explicitamente

name = "pepe"
print(type(name))

name = 123
print(type(name))

#tipado fuerte : no hace conversiones automaticas 

#print( 10 + "2") da type error 
print(f"Hola {my_name}, tengo {age} años") # f string (literal de cadena de formato), para meter variables dentro de una cadena

# Convenciones para nombrar variables
mi_nombre_de_variable = "ok" #snake case
nombre = "ok"
MiNombreDeVariable = "ko" #PascalCase
minombredevariable = "ko" #todojunto
MI_CONSTANTE = 3.14 # UPPER_CASE para constantes (no hay constantes reales en python, es una convención)

mi_nombre : str = "lele" # anotacion de tipos con :

