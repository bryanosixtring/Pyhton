#Files

# .txt files

import os
import json
import csv

file = open("files/file.txt", "r")

#print(file.read())
#print(file.read(10))
#print(file.readline())
#print(file.readlines())

for line in file.readlines():
    print(line)


#Escribir un archivo

txt_file = open("files/my_file.txt", "w+", encoding="utf-8")
txt_file.write("Mi nombre es John\nMi apellido es Senado")

txt_file.close()

#os.rename("files/my_files.txt","files/my_file1.txt")
#os.remove("files/my_file.txt")

# Archivos json

json_file = open("files/my_file.json", "w+",encoding="utf-8")

json_test = {
    "name":"John",
    "surname":"Senado",
    "Age":38,
    "Languages":["Python","C#","Javascript"],
    "Hobbies":["Videojuegos","Leer","Peliculas"]
}

json.dump(json_test,json_file,indent=0)
json_file.close()

with open("files/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
