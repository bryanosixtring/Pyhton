#Ciclos

#while

my_condition=0

while my_condition < 10:
    print(my_condition)
    my_condition += 1

else:
    print ("Mi condicion es mayor a 10")

print ("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecución")
        break
    print(my_condition)

#for

my_list = [35,24,62,52,30,30,17]

for element in my_list:
    print(element)


my_tuple= (35,24,62,52,30,30,17)

for element in my_tuple:
    print (element)

numeros=[]

for numero in range(1,21):
    numeros.append(numero)

print (numeros)

suma=0
for numero in numeros:
    suma+=numero

print (suma)