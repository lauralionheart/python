"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

texto = "RjrjRRjjjRRRrjjJJ"

def equilibrio (cadena):
    
    cadena_minus = cadena.lower()
    conteo_r = cadena_minus.count('r')
    conteo_j = cadena_minus.count('j')
    print(conteo_r)
    print(conteo_j)

    return conteo_r == conteo_j


print(equilibrio(texto))



"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""


lista_numeros = [1,3,4,6,9,12]

def huevos_dinos_carnivoros (lista):
    conteo = 0
    for i in lista:
        if i % 2 == 0:
            conteo += i
    return conteo

print(huevos_dinos_carnivoros(lista_numeros))



"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

nums = [4,5,6,2]
print(len(nums))

def suma (nums,goal):
    for i in nums:
        for j in range(i + 1, len(nums)):
         if nums[i] + nums[j] == goal:
             return[i,j]   


print(suma(nums,8))    

