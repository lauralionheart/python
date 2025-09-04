###
#La funcion input() permite obtener datos del usuario a traves de la consola


#print("Hola, ¿como te llamas?")
#nombre = input()

#print(nombre)

#Manera corta de hacer lo mismo
nombre = input("Hola ¿cómo te llamas?\n") #\n para salto de linea
print(f"Hola {nombre}, encantado de conocerte")
age = input("¿Cuántos años tienes? \n")
print(f"Dentro de 20 años vas a tener {int(age) + 20} años") #siempre que el usuario introduce datos con input() seran strings, hay que convertirlos a int en caso de numeros

ciudad,pais = input("¿De dónde eres? (ciudad, país)\n").split(",") # el metodo split() separa una cadena en varias partes, en este caso por la coma
print(f"Oh, {ciudad} es una ciudad preciosa, y {pais} un país genial")