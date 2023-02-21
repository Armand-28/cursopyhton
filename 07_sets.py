# Sets
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # esto inicialmente es un diccionario "dict"

my_other_set = {"Armando","Perdomo", 18, 1.75, "Arman"}
print(my_other_set)
print(type(my_other_set))


print(len(my_other_set))     # Un set no es una estructura ordenada

my_other_set.add("Millonario")  # Un set no abmite datos repetidos
print(my_other_set)

my_other_set.add("Campesino")  # con add() se pueden añadir datos siempre y cuando no esten repetidos
print(my_other_set)

print( "Armando" in my_other_set)
print( "Perdomo" in my_other_set)   # Con in se puede comprobar si un dato esta o no dentro del set
print( "dinero" in my_other_set)

my_other_set.remove("Campesino")
print(my_other_set) 

my_other_set.clear()
print(len(my_other_set))

#del my_other_set
#print(my_other_set)  #  name 'my_other_set' is not defined

my_set = {"Armando","Perdomo", 18, "tupuedes"}
my_list = list(my_set)
print(my_list)
print(type(my_list))
print(my_list[0])

print(18 in my_set)
print("Armando" in my_set)

my_other_set = {"javascrip", "css", "html", "python"}

my_sum_set = my_set.union(my_other_set)
print(my_sum_set.union(my_sum_set).union(my_set).union({"php", "java","c#"}))

print(my_sum_set.difference(my_set))

my_sum_set.difference_update(my_set)
print(my_sum_set)

my_sum_set.discard("python")
print(my_sum_set)

my_sum_set.add("hooo")
print(my_sum_set)

my_sum_set.discard("hooo")
print(my_sum_set)

pc = {"asus","lenovo","huawei"}
movil = {"redmi","samsung"}
print(movil)

movil.add("huawei")
print(movil)

movil.discard("huawei")
print(movil)

hola = movil.union(pc)
print(hola)

helo = hola.pop()
print(helo)

hola.remove("lenovo")
print(hola)

hola.clear()
print(hola)

hola.add("redmi")
print(hola)

hola.add("asus")
print(hola)

hola.update({"hola","lobo","perto"})
print(hola)










