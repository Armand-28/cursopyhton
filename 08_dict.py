# Dicionarios "dict"

my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

my_dict = {"Nombre":"Armando", "Apellido":"Perdomo", "edad":35}
print(my_dict["Nombre"])

my_other_dict = {"Nombre":"Armando",
 "Apellidos":"Perdomo",
 "Edad":18,
 "lenguajes":{"Python", "Javascrip", "Css"},
 1:1.75
 }
print(my_other_dict)
print(my_other_dict["lenguajes"])

print(len(my_other_dict))
print(len(my_dict))

my_dict["Nombre"] = "Eduardo"
print(my_dict["Nombre"])

my_dict["edad"] = 20
print(my_dict["edad"])

my_dict["Altura"] = 1.75
print(my_dict)

my_dict["Profesion"] = "Programador"
print(my_dict)

del my_dict["Altura"]
print(my_dict)

print( "Armando" in my_dict)
print( "Apellido" in my_dict)
print(my_dict["Profesion"])

print(my_dict.items())
#print(my_dict.fromkeys())
#print(my_dict.get())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.setdefault("edad"))
print(my_dict.fromkeys("ab",[my_dict]))

my_list = [ "Armando", "perdomo", 30]
print(my_list)

print(my_dict.fromkeys(my_list))

nueva = dict.fromkeys(my_list)
print(nueva)

nueva = dict.fromkeys((my_dict))
print(nueva)

nueva = dict.fromkeys(my_dict,"Juan")
print(nueva)

print(list(nueva))
print(tuple(nueva))
print(set(nueva))

nueva = list(my_other_dict)
print(nueva)                          #asi se pasa de un diccionario a un a una lista
print(type(nueva))

nueva.insert(2,{"Sexo":"Masculino"})
print(nueva)

nueva = dict(my_dict)                    # Asi se pasa de una listya a un diccionario
print(nueva)
print(type(nueva))

nueva = tuple(my_dict)
print(nueva)
print(type(nueva))
# my_dict = {"Nombre":"Armando",
# "Apellido":"Perdomo",
# "Edad":18
# }
# print(my_dict)

# print(my_dict.values())
# print(my_dict.keys())
# print(my_dict.fromkeys("Apellido",["Juan"]))
# print(my_dict.get("Nombre"))
# print(my_dict.items())
# my_dict.update([("Nombre","Armando"),("Apellido","Perdomo")])
# print(my_dict)
# print(type(my_dict))

# del my_dict["Apellido"]
# print(my_dict)

# my_dict["Apellido"] = "Perdomo"
# print(my_dict)

# my_dict["Profesion"] = "Programador"
# print(my_dict)


# my_lista = ["Armando","Perdomo",20]
# print(my_lista)

# print(my_dict.fromkeys(my_lista))

# new_list = dict.fromkeys(my_lista)
# print(new_list)
# print(type(new_list))

# new_list = dict.fromkeys(my_dict)
# print(new_list)

# nueva = dict(my_dict)
# print(type(nueva))      asi se pasa el diccionario a una nueva variable

# nueva["Jugador"] = "Cr7"
# print(nueva)

# print(nueva.clear())

# nueva["Jugador"] = "cristiano"  de esta manera borro todos los datos del diccionario y vuelvo a meter datos de cero
# print(nueva)

# copia = nueva.copy()
# print(copia)              De esta manera se logra hacer una copia del diccionario a una nueva variable

# print(copia.get("Jugador"))

repaso = {"Nombre":"Armando",
 "Apellidos":"Perdomo",
 "Edad":18,
 "lenguajes":{"Python", "Javascrip", "Css"},
 "Altura":1.75
 }

print(repaso)

del repaso["lenguajes"]
print(repaso)

repaso["Profesión"] = "Programdor"
print(repaso)

print(repaso.fromkeys(repaso))
print(repaso.get("Nombre"))
print(repaso.keys())
print(repaso.values())
print(repaso.items())
print(repaso.setdefault("Nombre"))

print("Profesión" in repaso)


diccionario = {"a":"ei","b":"bi","c":"ci","d":"di"}
print(diccionario)



print(diccionario.get("a"))

del diccionario["d"]
print(diccionario)


print(diccionario.items())

print(diccionario.keys())

print(diccionario.fromkeys(diccionario))

print(diccionario.values())

print(diccionario.update(diccionario))

print(diccionario.setdefault("b"))

# print(diccionario.popitem("a","b"))

print("El diccionario es sobre el abecedario :" + str(diccionario))

diccionario["d","e"] = {"di","i"}
print(diccionario)

del diccionario["d","e"]
print(diccionario)





