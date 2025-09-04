# Sentencias condicionales if, elif, else

#edad = 18
# La sintasis de python usa tabulaciones para definir bloques de codigo
#if edad >= 18:
    #print("Eres mayor de edad")
import os
os.system("clear")   ##importamos el modulo os para acceder al sistema y ejecutar el comando clear que limpie la consola en cada ejecucion

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")    
 

nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")   


#Operadores lógicos and, or, not

#and comprueba que todas las condiciones sean True                 
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet: 
    print("Puedes conducir")
else:
    print("DELINCUENTE!")

#or comprueba que al menos una condicion sea True, es como el || de otros lenguajes    

if edad >= 18 or tiene_carnet:
    print("Puedes conducir")   #un poco temerario pero bueno

#not invierte el valor booleano, es como el ! de otros lenguajes

if not tiene_carnet:
    print("No puedes conducir, no tienes carnet")
