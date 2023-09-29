#functions

#Definición

def my_function():
    print("Esto es una función")

my_function()


    #Función con parámetros de entrada/argumentos

def sum_values(primer_valor, segundo_valor):
    print(primer_valor+segundo_valor)


primer_valor = 10
segundo_valor = 4

sum_values(primer_valor,segundo_valor)

def print_name(name,surname):
    print(f"{name} {surname}")

print_name(surname="Sedano",name="Jhon")


def print_name2(name,surname,alias):
    print(f"{name} {surname} {alias}")

print_name2("Jhon","Sedano","JS")

def print_upper_text(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_text("Hola", "JHON", "Python", "Sedano")