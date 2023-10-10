
import re
my_string = "Esta es la lección número 18: Lección llamada Expresiones"

my_other_String = "Esta no es la lección número 5: Manejo de Tuplas"

#Match()

print(re.match("Esta es la lección", my_string))

match= re.match("Esta es la lección", my_string,re.I)

print(match.span())

#search

search = re.search("lección", my_string, re.I)
print(search)

#findall()

findall = re.findall("lección", my_string, re.I)
print(findall)

#split

print(re.split(":", my_string))

#sub

print(re.sub("Expresiones Regulares","RegEx", my_string))
print(re.sub("[l][L]ección","LECCIÓN", my_string))

#patterns

pattern = r"[lL]ección"

print(re.findall(pattern,my_string))

pattern = r"[0-9]"

print(re.findall(pattern,my_string))


