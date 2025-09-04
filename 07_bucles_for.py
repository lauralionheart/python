#bucle de codigo que se ejecuta repetidamente mientras itera un iterable o una lista

print("Bucle for:")
#iterar sobre una lista
frutas = ['naranja', 'platano', 'manzana', 'pera']

for frutas in frutas:
    print(frutas)
    

#Iterar sobre una cadena
nombre = "laura"  

for letra in nombre:
    print(letra)


#enumerate() para cuando queremos saber el indice de cada elemento

frutas = ['naranja', 'platano', 'manzana', 'pera']    

for index,fruta in enumerate(frutas):    # primero el indice(posicion) y luego el valor
    print(f"El indice es {index} y la fruta es {fruta}")


#bucles anidados

letras =  ['A', 'B', 'C']
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")


# break

animales = ["perro","gato","raton","loro","pez","canario"]
#vamos a encontrar al loro
for index,animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta en el indice {index}")
        break #cuando encontramos al loro, salimos de la iteracion con el break
        



#Comprension de listas 

animales = ["perro","gato","raton","loro","pez","canario"]     

animales_mayus = [animal.upper() for animal in animales] # para hacer el for en una sola linea
print(animales_mayus)


