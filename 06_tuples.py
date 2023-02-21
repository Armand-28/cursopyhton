# Tuplas

my_tuples = tuple()
my_other_tuple = ()

my_tuples = (18, 1.75, "Armando", "Perdomo", 18) # ejemplo aqui hay 3 valores positivos y de forma negativa hay 4 
print(my_tuples)
print(type(my_tuples))

my_other_tuple = (25, 30, 45, 20)

print(my_tuples[2])
print(my_tuples[3])
print(my_tuples[0])
print(my_tuples[-4])
print(my_tuples[-1])
#print(my_tuples[-1])  Index error
#print(my_tuples[-1])  Index error                          # siermpre que sea positivo se cuenta de 0 y si es negativo se cuenta de -1


print(my_tuples.count(18))
print(my_tuples.index("Armando"))

 # my_tuples[1] = 160   el objeto "tupla" no admite la asignación de elementos
 # print(my_tuples)

print( my_tuples + my_other_tuple)

my_new_tuple = my_other_tuple + my_tuples
print(my_new_tuple)

print(my_new_tuple[2:7])

my_tuples = list(my_tuples)
print(type(my_tuples))

my_tuples[4] = "Arki" 
my_tuples.insert(1, "azul")

my_tuples = tuple(my_tuples)
print(my_tuples)
print(type(my_tuples))

my_other_tuple = list(my_other_tuple)
print(my_other_tuple)
print(type(my_other_tuple))

my_other_tuple[2] = "arki"
my_other_tuple.append("Edades")
my_other_tuple.insert(5, 180)
print(my_other_tuple)

my_other_tuple = tuple(my_other_tuple)
print(my_other_tuple)
print(type(my_other_tuple))

del my_tuples   # En las tuplas no se puede hacer ninguna modificacion
# print(my_tuples)     # el nombre 'mis_tuplas' no está definido





my_juan = ("hola", "sera", 4, 120)
print(my_juan)
print(type(my_juan))

print(my_juan.count("sera"))

print(my_juan.index(4))

