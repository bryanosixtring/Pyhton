#Sets
my_set = set()
my_other_set = {}

my_other_set = {"John","Sedano",38}

print(my_other_set)

my_other_set.add("JS")

print(my_other_set)

#Búsqueda

print("Sedano" in my_other_set)

#Eliminar

my_other_set.remove("Sedano")


my_set.add(1)
print(my_set)
my_new_set = my_set.union(my_other_set)

