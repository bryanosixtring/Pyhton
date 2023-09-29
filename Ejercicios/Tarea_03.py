#Tarea 3:

import random

nombreplayer = input("¿Hola, cómo te llamas?")

numero = random.randint(1,20)

print(nombreplayer, ",Estoy pensando en un número del 1 al 20")

intentos = 0

while intentos < 6:
    print("Intenta adivinar")
    opcion = int(input())

    intentos = intentos+1

    if(opcion < numero):
        print("Es un número mayor")
    elif(opcion > numero):
        print("Es número es menor")
    elif(opcion == numero):
        break

if(numero==opcion):
    print("Muy bien",nombreplayer,", has adivinado el número en ",intentos," intentos")

else:
    print("Perdiste, el número que pensé fue el ",numero)

    


