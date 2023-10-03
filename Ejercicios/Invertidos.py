"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

"""

str = input('Ingresa la frase')

fraselong = len(str)

inversa=[]

while fraselong > 0:
    inversa += str [fraselong-1]
    fraselong = fraselong - 1

texto = ''.join(inversa)
print('La frase inversa es: ',texto) 