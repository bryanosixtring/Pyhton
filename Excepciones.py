#Excepciones

number_one = 5
number_two = 2
number_two = "2"

#print(number_one + number_two)

try:
    print(number_one + number_two)
    print("No se ha producido un error")

except:
    print("Se ha producido un error")


#flujo completo de una excepción: try-except-else-finally

try:
    print(number_one + number_two)
    print("No se ha producido un error")

except:
    print("Se ha producido un error")

else:
    print("La ejecución continua correctamente")

finally:
    print("La ejecución finaliza")

#captura de errores

try:
    print(number_one + number_two)
    print("No se ha producido un error")

except TypeError as error:
    print("Se ha producido un error")
    print(error)

except ValueError as error:
    print(error)

except Exception as error:
    print(error)

#convertir cadena que no es número

try:
    numero = int("abc")

except ValueError as e:
    print("Occurió un ValueError: ", str(e))

