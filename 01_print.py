print("HOLA MUNDO") # print() imprime en consola 
print('cadena con una comilla') # las strings podemos hacerlas con " " y con ' '
print("python", "es", "guay") # podemos imprimir varias cosas separadas por comas 
print("python", "es", "chulo", sep="-") # podemos añadir un separador con sep 
print("hola", end=" ") # aqui no hay salto de linea, con end le hemos dicho que acabe con un espacio
print("que tal") # por defecto end es un salto de linea end = "\n"
print(type(10)) # la funcion type() nos dice el tipo de dato
print(3+2) # podemos hacer operaciones dentro del print
print(type(3.14)) # en python los decimales son tipo float
print(type(1.0)) 
print(type(1e3)) # esto es notacion cientifica 1 x 10 al cubo = 1000.0, siempre que hay una notacion cientifica es float
print(type(1 + 2j)) # los numeros complejos en python se representan con j
print(type(True))
print(type(False)) #los booleanos son True y False
print(type(1<2)) # las comparaciones devuelven booleanos
print(type(None))# None es un tipo especial que representa la ausencia de valor, algo entre null y undefined en otros lenguajes

##############################

#Transformar un tipo de un valor a otro. Python no hace conversiones automaticas de tipos que no son compatibles

print("Conversión de tipos")
print(type("100")) 
print(2 + int("100"))# Convertimos con int() la cadena "100" para que se pueda sumar, ya que no podemos sumar un int y una string
print("100" + str(2))

print(bool(1))
print(bool(0)) # el unico int que es False es el 0, el resto aunque sean numeros negativos, son True
print(bool(-1))