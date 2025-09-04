import os
os.system("clear")

lista1 = [1, 2, 3, 4, 5]

lista2 = lista1 + [6, 7]  # concatenacion menos eficiente
lista2 += [8, 9] #concatenacion mas eficiente
lista3 = ["string", 10, 2.32, True] #la lista puede contener diferentes tipos de datos
print(lista2)

print("longitus de lista2 es: ", len(lista2))

#slicing de listas   [desde:hasta:paso]

print(lista2[1:4]) #imprime desde el indice 1 (que es 2) hasta el indice 4 (que es el 5, pero este no se incluye)
print(lista2[:3]) #imprime desde el inicio hasta el indice 3 (el ultimo no se incluye)
print(lista2[2:]) #imprime desde el indice 2 hasta el final
print(lista2[:]) # imprime una copia de toda la lista

print(lista2[::2]) # nos va dando los indices que sean pares
print(lista2[::-1]) # devuelve la lista al reves ya que ponemos un paso negativo


#modificar lista

lista2[0] = 20
print(lista2)



#metodos para las listas


lista = [1,2,3,4,5]

lista.append(6) #añade un elemento al final de la lista

lista.insert(1, 1.5) #inserta un elemento en la posicion indicada primeramente, desplazando el resto de elementos a la derecha
print(lista)

lista.extend([7, 8]) #agrega elementos al final de la lista

lista.remove(1.5) #elimina la primera aparicion del elemento que indiquemos
print(lista)

ultimo = lista.pop() #elimina el ultimo elemento de la lista y lo devuelve

print(ultimo)
print(lista)

lista.pop(1) #elimina el segundo elemento de la lista ( el que esta en el indice 1)
print(lista)

del lista[-1] #elimina el ultimo elemento de la lista usando del
print(lista)

lista.clear() #elimina todos los elementos de la lista
print(lista)

listita = ['koala', 'panda', 'zorro', 'leon', 'tigre', 'panda']
del listita[1:3] #elimina los elementos desde el indice 1 hasta el 3 (el 3 no se incluye)
print(listita)
print(listita.count('panda')) #cuenta cuantas veces aparece el elemento en la lista

## otros metodos
print("ordenar listas modificando la original")
numbers = [2,5,1,0,9]
numbers.sort() #ordena la lista de menor a mayor, aqui modifica la lista original y la ordena pero no devuelve nada
print(numbers)


print("ordenar listas creando una nueva")
numbers = [2,5,1,0,9]
sorted_numbers = sorted(numbers) #ordena la lista de menor a mayor y devuelve una nueva lista ordenada
print(sorted_numbers)

frutas = ['naranja', 'pera', 'manzana', 'kiwi']

print("Ordenar lista de cadenas en minuscula;")
sorted_frutas = sorted(frutas) #la ordena alfabeticamente
print(sorted_frutas)

frutites = ['Naranja', 'pera', 'Manzana', 'kiwi']
print("Ordenar lista de cadenas dodne haya mayusculas y minusculas:")

frutites.sort(key=str.lower) #ordena la lista ignorando las mayusculas y minusculas (pasamos todo a minusculas)
print(frutites)
