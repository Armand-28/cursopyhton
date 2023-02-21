# list
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [18 , 34, 28, 15, 16, 18, 26]
print(my_list)
print(len(my_list))

my_other_list = [18, 175, "Armando", "perdomo"]
print(my_other_list)
print(type(my_other_list))

# Acceso a elementos de busquedad

print(my_other_list[0])
print(my_other_list[3])
print(my_other_list[-4])
print(my_other_list[-3])
print(my_other_list[-1])
print(my_other_list.count("perdomo"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2],my_other_list[1], my_other_list[0], my_other_list[3]
print(surname)



print(my_list + my_other_list)
print(my_list, my_other_list)


my_other_list.append("Armando")
print(my_other_list)

my_other_list.insert(3, "azul")
print(my_other_list)

my_other_list[3] = "rojo"
print(my_other_list)

my_other_list.remove("rojo")
print(my_other_list)

my_list.remove(18)
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.pop(4))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[1]
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[0:2 ])

my_list = "hola python"
print(my_list)

my_lista = ["futbol", 35,"experiencia"]

sport, expe, age,  = my_lista[0], my_lista[2], my_lista[1]
print(sport)

my_tu = tuple(my_lista)
print(my_tu)
print(type(my_tu))


print(my_tu.index("experiencia"))

my_tu = list(my_lista)
print(my_tu)

my_tu.insert(2, "millonario")
print(my_tu)

my_tu.append(["hola", "que mas", "nex lista"])
print(my_tu)

my_tu.reverse()
print(my_tu)

print(my_tu.pop(4))
print(my_tu)

my_new_pop = my_tu.pop(2)
print(my_new_pop)
print(my_tu)

nueva_tupla = ("Armando","Karina","Flor","Mima")
print(nueva_tupla)

print(nueva_tupla.index("Karina"))

nueva_tupla = list(nueva_tupla)
print(type(nueva_tupla))

nueva_tupla.insert(2, "Mama")
print(nueva_tupla)

nueva_tupla.append("papa")
print(nueva_tupla)

nueva_tupla[3] = "cathe"
print(nueva_tupla)

copia = nueva_tupla.copy()
print(copia)

nueva_tupla.clear()
print(nueva_tupla)
print(copia)

copia.extend(["nathy","erika"])
print(copia)

copia = tuple(copia)
print(copia)
print(type(copia))

lista = ["uno","dos","tres","cuatro"]
print(lista)

lista.insert(4,"cinco")
print(lista)

lista.append("seis")
print(lista)

print(lista.pop(5))
print(lista)

lista.remove("cinco")
print(lista)

del lista[1]
print(lista)

lista[0] = "dos"
print(lista)

copia_lista = lista.copy()
print(copia_lista)

lista.clear()
print(lista)
print(copia_lista)


copia_lista = tuple(copia_lista)
print(copia_lista)
print(type(copia_lista))

copia_lista = set(copia_lista)
print(copia_lista)
print(type(copia_lista))

copia_lista = dict({1:"uno",2:"dos"})
print(copia_lista)
print(type(copia_lista))


orden = ["1","2","3","4"]
print(orden)

orden.append("5")
print(orden)

orden.insert(0,"0")
print(orden)

orden.extend(["6","7"])
print(orden)

orden.index("1")
print(orden)

print(orden.pop(4))

print(" ")

orden.remove("6")
print(orden)

del orden[1]
print(orden)

copy = orden.copy()
print(copy)

orden.clear()
print(orden)

print(copy)
copy[2] = "4"
print(copy)





