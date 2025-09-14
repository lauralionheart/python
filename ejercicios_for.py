# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

for numero in range (2,20,2):
    print(numero)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

numeros = [10,20,30,40,50]
total = 0
for numero in numeros:
    total += numero
    
media = total/len(numeros)
print(media)


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\n Ejercicio 3 de bucles for")

numeros = [15,5,25,10,20]

numero_mayor = 0

for numero in numeros:
    if numero > numero_mayor:
        numero_mayor = numero

print(numero_mayor)


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]

nueva_lista = []

for palabra in palabras:
    if len(palabra) > 5:
        nueva_lista.append(palabra)

print(nueva_lista)   


# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

print("Ejercicio 5: \n")

palabras = ["casa","arbol","sol","elefante","luna","coche"]

letra = input("Introduce una letra \n").lower()
contador = 0
for palabra in palabras:
    if palabra.startswith(letra):
        contador += 1

print(contador)