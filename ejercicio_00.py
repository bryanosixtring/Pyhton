#Piedra, papel o tijera

#Definir unas variables

#piedra =1, papel =2, tijera =3

piedra = 1
papel = 2
tijera = 3

print("Por favor escoger una opción:")
print("1 Piedra")
print("2 Papel")
print("3 Tijera")

jugador1=input("Elija jugador 1 ")
jugador2=input("Elija jugador 2 ")

"""
J1 J2 RJ1
1  1   e
1  2   p
1  3   g
2  1   g
2  2   e
2  3   p
3  1   p
3  2   g
3  3   e

"""

if(jugador1 == jugador2):
    print("Empate")

elif(jugador1==1 and jugador2==3) or (jugador1==2 and jugador2==1) or (jugador2==1) or (jugador1==3 and jugador2==2):
    print("El jugador 1 gana")

else:
    print("El jugador 2 gana")