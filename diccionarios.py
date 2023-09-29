#diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_other_dict))

my_other_dict = {"Nombre" : "Jhon", "Apellido": "Sedano", "Edad":38,1:"Python"}
print(my_other_dict)

my_dict = {
"Nombre" : "Jhon", 
"Apellido": "Sedano", 
"Edad":38,
"Lenguajes" : {"Python","Java","C#"},
"Altura":1.55

}
print(my_dict)

print(len(my_dict))

#Inserción

my_dict["Alias"] = "JS"
print(my_dict)

my_dict["Nombre"] = "Jairo"
print(my_dict)

print(my_dict.items())
print(my_dict.values())
print(my_dict.keys())

