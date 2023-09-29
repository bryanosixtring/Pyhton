#Tarea 2:

edad = int(input("Escriba por favor su edad"))

if (edad < 18):
    print(" Categoría: Niño")
elif(edad >= 18 and edad <= 30):
    print(" Categoría: Joven")
elif(edad > 30 and edad <= 50):
    print(" Categoría: Adulto")
elif(edad >50 and edad <70):
    print(" Categoría: Señor")
elif(edad >= 70):
    print(" Categoría: Master")

