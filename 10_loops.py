## Loops##
# bucle = 0

# while bucle <= 20:
#     print(bucle)
#     bucle += 2

# lista = [1,2,3,4,5]

# for numero in lista:
#     print(numero)
#     print(lista)

# n = 0

# while n < 20:
#     print(n)
#     n += 5


# my_condition = 0

# while my_condition < 20:
#     print(my_condition)
#     my_condition += 2


# print("ya se cumple mi condicion")

#Bucle while#

my_while = 0

while my_while < 10:
    print(my_while)
    my_while += 2 
else:
    print("Mi condicion es mayor o igual que 10")

print("Le ejecucuion termino")



while my_while < 20:
    my_while += 1

    if my_while == 15:
        print("Mi condicion es igual a 15")
        break

    print(my_while)

print("La ejecución acaba")    

mi_condicion = 0

while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 19:
        print("mi condicion se detiene")
        break


    print(mi_condicion)

print("hollaa")
repaso = 0

while repaso < 100:
    repaso += 1
    if repaso == 99:
        print("fin de la condición")
        break                                        #La funcion break cumple con parar nuestro bucle tanto en el for como while#




    print(repaso)


## Bucle For ##

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numeros in my_list:
    print(numeros) 
else:
    print("fin de la lista")   


my_tuples = (18, 1.75, "Armando", "Perdomo", 18)

for numeros in my_tuples:
    print(numeros)

my_set = {"Armando","Perdomo", 18, 1.75, "Arman"}

for numeros in my_set:
    print(numeros)

my_dict = {"Nombre":"Armando",
 "Apellidos":"Perdomo",
 "Edad":18,
 "lenguajes":{"Python", "Javascrip", "Css"},
 "Altura":1.75
 }
for numeros in my_dict.items():
    print(numeros)
    if numeros == "Edad":
        break
else:
    print("el bucle ha terminado")    


print("continua el diccionario")
    

my_tupla = (18, 1.75, "Armando", "Perdomo", 18)

for caracteristicas in my_tupla:
    print(caracteristicas)
    if caracteristicas == "Perdomo":
        break

else:
    print("fin de la tupla")

print("fin de la tupla")


marcas_car = ["Mazda","Mercedes","Audi","Toyota","Chevrolet"]

for marcas in marcas_car:
    print(marcas)
    if marcas == "Toyota":
        break

else:
    print("fin de la lista")

print("Fin de la lista de carros")


mar_car = ["Mazda","Mercedes","Audi","Toyota","Chevrolet"]

for car in mar_car:
    print(car)
    if car == "Toyota":
        break

print("fin de la marcas")


x = 0

while x < 10:
    x += 1
    if x == 9:
        break
    print(x)


print("fin de la ejecución")


my_list = [18 , 34, 28, 15, 16, 18, 26]

for numeros in my_list:
    print(numeros)
    if numeros == 16:
        break

else:
    print("fin de la lista numeros") 

print("fin de la propiedad")       

my_dictionary = {"Nombre":"Armando",
 "Apellidos":"Perdomo",
 "Edad":18,
 "lenguajes":{"Python", "Javascrip", "Css"},
 "Altura":1.75,
 "sexo":"Masculino"
 }

for dict in my_dictionary.items():
    print(dict)
    if dict == ("Altura",1.75):
        break
else:
    print("fin del diccionario")    

repaso = 0

while repaso < 100:
    repaso += 2
    print(repaso)
else:
    print("Mi condicion es menor o igual que 100")

print("fin de la condicion 100")

while repaso < 200:
    repaso += 1
    
    if repaso == 195:
        print("mi condicion es menor o igual a 195")
        break
    print(repaso)


print("fin de la condicion 200")


tablas = 0

while tablas < 100:
    tablas += 1
    if tablas == 99:
        break   
    print(tablas) 
print("fin de la tabla")


ejercicio = {"uno =":"one","dos =":"two","tres =":"three","cuatro =":"four"}

for numeros in ejercicio.items():
    print(numeros)
    if numeros == ("tres =", "three"):
        break 
else:
    print("fin del diccionario") 

print("Fin de la propiedad") 


variable = 0

while variable < 12:
    variable += 1
    if variable == 10:
        break
    
    print(variable)

print("fin de la condicion while")

ciclos = {
    "Nombre":"Armando",
    "Apellido":"Perdomo",
    "Edad":18,
    "Lenguages":{"html","css","python","php","mysql","javascrip","django"},
    "Profesion":"programador",
    "Meta":"ser el mejor programador"
}


for dict in ciclos.items():
    print(dict) 
    if dict == ('Profesion', 'programador'):
        break
    
else:
    print("fin del ciclo for")

print("fin de la condicion for")


colores ={"negro":"black","blanco":"white","amarillo":"yellow","azul":"blue"}

for colors in colores.items():
    print(colors)
    if colors == ('amarillo', 'yellow'):
        break

print("fin del ciclo for de colores")


quest = 0

while quest < 250:
    quest += 1
    print(quest)
    if quest == 249:
        break
print("se detiene el bucle")

lista_chequeo = [1,2,3,4,5,6,7,8,9,10,12,14,15,18]

for numero in lista_chequeo:
    print(numero)
    if numero == 15:
        print("esat dentro de la lista")
        break
else:
    print("no esta dentro")

talcos = 0

while talcos < 24:
    talcos += 1
    print(talcos)
    if talcos == 17:
        break

print("precio de los talcos")

n1 = 1

while n1 <= 100:
    if n1 % 2 == 0:
        print(f"{n1} Es par")
    
    else:
        print(f"{n1} Es impar")
    n1 += 1



for num in range(1,101):
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} Es impar")


number = int(input("Introduce el numero :"))

while number != 0:
    if number % 2 == 0:
        print(f"El numero {number} es par")
    else:
        print(f"El numero {number} es impar")
    number = int(input("Si no desea seguir oprime el numero 0: \n"))

