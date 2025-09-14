
#permite crear una secuencia de numeros

nums = range(5) #esto no crea una lista, range(inicio,fin,paso)

for num in nums:
    print(num)


for num in range(5,10):
    print(num)   


for num in range(10,20,2): #de 2 en 2
    print(num)   



# si queremos hacer una lista

nums = range(10)

list_of_nums = list(nums)  #con list()
print(list_of_nums)