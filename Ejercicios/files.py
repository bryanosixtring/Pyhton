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

#obtener datos de un archivo json
json_dict = json.load(open("files/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])
print(json_dict["Languages"])

#csv files

csv_file = open("files/my_file.csv","w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","language"])
csv_writer.writerow(["John","Sedano",38,"Python"])
csv_writer.writerow(["Jairo","Segura",40])

csv_file.close()

with open("files/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)