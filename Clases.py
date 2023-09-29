#classes

#Definición

class Person:
    def __init__(self, name, surname, edad):
        self.nombre = name
        self.apellido = surname
        self.edad = edad
        self.alias = "Sin Alias"
    
    def presentacion(self):
        print(f"{self.nombre} {self.apellido}")
    
    def get_name (self):
        return self.__name
    
    def set_name(self, nuevonombre):
        self.__name = nuevonombre

my_person1 = Person("Jhon","Sedano",38)

print(my_person1.apellido)

my_person2 = Person("Pepito","FFF",18)

my_person1.presentacion()

print("Hola")


