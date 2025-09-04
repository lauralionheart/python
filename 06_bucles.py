#bucles (while)

contador = 0

print("Bucle while:")
while contador < 5: #mientras contador sea menor que 5
    print(contador)
    contador += 1

print("Bucle con while break:")
while contador < 10:    #cuando no sabemos cuantas veces se va a repetir el bucle
    print(contador)
    contador += 1
    if contador == 5:
        break      #sale del bucle
         

######
print("Bucle con while continue:")
contader = 0
while contader < 10:
    contader += 1
    if contader % 2 == 0:
        continue   #salta a la siguiente iteracion del bucle, da igual lo que haya debajo
    
    print(contader)


#else, esta condicion cuando se ejecuta?

print("Bucle while con else:")

contadir = 0
while contadir < 5:
    print(contadir)
    contadir += 1
else:   # cuando queremos asegurarnos de que la condicion del while es falsa 
    print("El bucle ha terminado")



#queremos pedirle al usuario un numero positivo

numero = -1

while numero < 0:
    try:   ## ponemos un try except para controlar que el usuario meta un numero o no, si no es un numero entonces salta al except
        numero = int(input("Introduce un numero positivo:"))
        if numero < 0:
            print("El numero tiene que ser positivo cariño mio")
    except:
        print("tiene que ser un numero >:(")
    

print(f"EL numero que has introducido es {numero}")
 

     

 