#Condicionales#
# edad = 18

# if edad < 18 :
#     print("Menor de edad")    Ejercicio para saber si es mayor de edad

# else:
#     print("Mayor de edad")


# edad = 17

# if edad >= 18 and edad < 50:
#     print("Mayor de edad")

# elif edad >= 50 :
#     print("Adulto mayor")

# else:
#     print("Menor de edad")

# number = [1,2,3,4,5]

# # x = 4

# # if x in number:
# #     print(f"El numero esta en la lista")           Ejercicio para saber si el numero esta en la lista
                                                         
# # else:
# #     print(f"El numero no esta la lista")    

my_condition =True

if my_condition:
    print("Se cumple la ejecución del if")


my_condition = 5 * 7

if my_condition == 15 :
    print("la respuesta es correcta1")


if my_condition > 15 and my_condition < 30 :
    print("es mayor que 15 y menor que 30 ")
elif my_condition == 35:
    print("Es igual a 35")
else:
    print("es menor o igual que 15 o mayor e igual a 30 o distinto de 25")

print("Sigue la ejecución") 


my_ejercicio = 5 + 95

if my_ejercicio > 15 and my_ejercicio < 25:
    print("es mayor que 15 o menor e igual que 25")

elif my_ejercicio == 100:
    print("Es igual a 100")

else:
    print("es menor o igual  que 15 o mayor e igual que 25")  


my_string = ""

if not my_string:
    print("mi cadena de texto es vacia")

if my_string == "mi cadena oooooo":
    print("estas cadena de texto no coinciden")

# else:
#     print("La respuesta es incorrecta") 


my_variable = ["Karina","Armando","Flor","Eduardo","Cathe"]

x = "amor"

if x in my_variable:
    print(f"El nombre esta en mi variable")

elif x == "amor":
    print("quiero a karina")    

else:
    print(f"El nombre  no esta en mi variable")


name= "Armando", "perdomo", 18, 75,"mama"

x = "Armando"

if x in  name:
    print(f"Esta dentro de la variable")

elif x == "Karina":
    print(f"Mama esta en la variable")    

else:
    print(f"No esta dentro de  la variable")    


adulto = 51

if adulto >= 18 and adulto <= 50:
    print("Es adulto")

elif adulto > 50:
    print("Adulto-mayor")    

else:
    print("Menor de edad") 

motos =  180 

x = 220

if motos > x and x < motos: 
    print(f"Pulsar es la mas veloz")

elif x >= 225:
    print(f" XT  es la mas veloz")

else:
    print(f"Pulsar no es la mas veloz")


pulsar = 900
discover = 125
xt = 100

if xt > pulsar and discover < pulsar and xt > discover:
    print("Xt es la mas veloz")

elif discover > pulsar and discover > xt:
    print("Discover es la mas veloz")

else:
    print("pulsar es la mas veloz")    


repaso = {"Nombre":"Armando",
 "Apellidos":"Perdomo",
 "Edad":18,
 "lenguajes":{"Python", "Javascrip", "Css"},
 "Altura":1.75
 }

x = "Karina"

if x in repaso:
    print("Esta dentro del diccionario")

elif x == "Karina":
    print(" si buenas")    

else:
    print("No esta en el diccionario")    

seg_repaso = 31 + 10

if seg_repaso >= 20 and seg_repaso <= 40:
    print("Adulto normal")

elif seg_repaso >40:
    print("Adulto mayor")

else:
    print("Es un joven")



nueva = 5 * 10

if nueva >= 18 and nueva < 50:
    print("la persona es mayor de edad") 

elif nueva >= 50:
    print("la persona ya es vieja")

else:
    print("la persona es menor de edad")

cb = 110
duke = 250
z_mil = 1000

if z_mil > duke and duke > cb and cb < z_mil:
    print("z_mil es la moto mas veloz")

elif cb > duke and cb > z_mil:
    print("cb es la moto mas veloz")

else:
    print("duke es la moto mas veloz")


armando = 50

if armando >= 18  and armando < 50:
    print("Armando es mayor de edad")

elif armando >= 50:
    print("Armando ya es adulto mayor")

else:
    print("Armando no es mayor de edad")


vel_max = 121

if vel_max >= 120 and vel_max <= 250:
    print("El motociclista va con sobrevelocidad")

elif vel_max <= 60:
    print("El usuario va despacio")

else:
    print("El motociclista va a una velocidad promedio")

colores = {"rojo":"sangre","azul":"agua","amarillo":"oro"}

x = 2

if x in colores:
    print("el color esta dentro de la variable")

elif x  == 2:
    print("es un umero no hace parte de esta condicion")

else:
    print("el color no esta dentro de la variable")


tupla = "Hola "

if not tupla.isalpha():
   print("Esta es una cadena sin numeros")

elif int( tupla.isnumeric()):
    print("esta variable contiene numeros")

else:
    print("Esta es una cadena")        

# -Escribe un programa que muestre por consola (con un print) los
# -números de 1 a 100 (ambos incluidos y con un salto de línea entre
# -cada impresión), sustituyendo los siguientes:
# -Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)