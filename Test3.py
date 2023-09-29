#listas

my_lista= list()
my_other_listo=[]



my_list=[35,24,62,52,30,30,17]

print(len(my_list))

my_other_list=[38,1.85,"John","senado"]
print(len(my_other_list))

#acceso a elttttttementos y búsqueda

print(my_other_list[-1])

print(my_list.count(35))

print(my_other_list.index("John"))

my_other_list.append("JS")
print(my_other_list)

my_other_list.insert(1,"Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

del my_list[2]
print(my_list)

#operaciones

my_new_list=my_list.copy()

my_list.clear()
print(my_list)

my_new_list.sort()
print(my_new_list)

#sublistas

print(my_new_list[1:3])


