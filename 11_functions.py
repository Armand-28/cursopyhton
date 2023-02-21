##Funciones##

# def my_function ():
#     name = "Armando"
#     surname = "Perdomo"
#     space = " "
#     age = 18
#     height = 1.75
#     todo = name + space + surname + space + str(age) + space + str(height)
#     print(todo)
# my_function()    

# def suma_num ():
#     num1 = 4
#     num2 = 6
#     return num1 * num2
# print(suma_num()) 
    
# def suma_num (num1,num2):
#     return num1 * num2      <==   esta es la mejor manera de hacerlo
# print(suma_num(3,5))
# 


# def suma_num (num1,num2):
#     print( num1 * num2)
# area = suma_num(3,8)

# def nombres ():
#     name = "flor"
#     name2 = "cathe"
#     name3 = "mima"
#     space = " "
#     name_123 = name + space + name2 +  space + name3 
#     return name_123
# print(nombres())
   
# def area_triangulo (b,h):
#     return b * h / 2
# area = area_triangulo(5,9)
# print(area)

# def area_circulo (r):
#     pi = 3.14
#     return pi * r ** 2
# print(area_circulo(10))  


def area_triangulo (b,h):
    return b * h / 2                     #<==  esta es la manera mas corta de hacerlo #
print(area_triangulo(5,8))

def area_circulo (pi,r):
    return pi * r ** 2                   #<==  esta es la manera mas corta de hacerlo #
print(area_circulo(3.14,12))  

def area_circulo (pi,r):               #<==  esta es la manera mas compleja ya qye hay que llamr una nueva variable pero seria correcto hacerlo asi tambien #
    return pi * r ** 2
area = area_circulo(3.14,12)
print(area)    

def nombres (name1,name2,name3):
    print(f"{name1} {name2} {name3}")
    
nombres(name1="flor",name2="cathe",name3="mima")
# formula area de un triagulo
def area_t (b,h):
    return b * h / 2
print(area_t(4,6))   

# formula del area de un circulo
def area_c (pi,r):
    return pi * r ** 2
print(area_c(3.1416,10))

# formula del teorema de pitagoras
import math
def hipotenusa (cateto1,cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

print("la hipotenusa es:",hipotenusa(2,4))


import math

def h (c1,c2):
    return math.sqrt(c1**2 + c2**2)

print("la hipotenusa es:",h(3,4))
print("la hipotenusa es:",h(4,5))

import math

def c (h,c2):
    return math.sqrt(h**2 - c2**2)

print("el cateto es:",c(5,4))
print("el cateto es:",c(6,3))


import math

def hipote (cate1,cate2):
    return math.sqrt(cate1**2 + cate2**2)

print("la hipotenusa es:",hipote(8,6))


def nombres (name,surname,age):
    print(f"{name} {surname} {age}")

nombres(age = 18,name = "Armando",surname = "perdomo")

def deporte (natacion,futbol,voleibol = "sin deporte"):
    print(f"{natacion} {futbol} {voleibol}")

deporte(futbol = "luis", natacion ="juan")


def listado_nombres (*listado):
    for cadena in listado:
        print(cadena.upper())       

listado_nombres("a","b","c","d","e","f")


import math

def hipotenusa (cateto1,cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

print("La hipotenusa es:",hipotenusa(8,6))

import math

def cateto (hipo,cat1):
    return math.sqrt(hipo**2 - cat1**2)

print("el cateto es:",cateto(6,4))

def equipos (name,surname,age):
    print(f"{name} {surname} {age} ")

equipos(name = "armandini", age =18, surname = "Perdomo")


def habitos (bueno,malo,regular = "ningun metodo"):
    print(f"{bueno} {malo} {regular}") 

habitos(bueno="Leer todos los dias:\n",malo="no tener accion:\n")  


def atomicos (*atomo):
    for big in atomo:
        print(big.capitalize())

atomicos("celula","atomo","bacterias","virus")

def metros (mul1,mul2):
    return mul1 * mul2
print(metros(16,7000))


def demora (km,a):
    return (km / a)

print("el tiempo que se demoro es recorrer maria 275_km es: ",demora(325,45))

def name (name_1,name_2,name_3):
    print(f"{name_1} {name_2} {name_3}")

name( name_2="Armando",name_1="karina",name_3="Daniela")

def valor_i (valor1,valor2,valor3 = "Gratis"):
    print(f"{valor1} {valor2} {valor3}")

valor_i(valor2="12.000k",valor1="10.000k")
 
def ejercicio (*ejerci):
    for diccionary in ejerci:
        print(diccionary.upper())
        

ejercicio("uno","one","dos","two","tres","three","cuatro","four")        


def for_triangulo(b,h):
    return b * h / 2

print("El area del trinagulo es igual:",for_triangulo(6,4))

def for_circulo (pi,r):
    return pi * r ** 2

print("el area de circulo:",for_circulo(3.14,12))

import math

def teorema_pi(cateto1,cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

print("la hipotenusa es:",teorema_pi(5,6))

import math

def for_teoreoma (hipotenusa,cateto1):
    return math.sqrt(hipotenusa**2 - cateto1**2)

print("El cateto es:",for_teoreoma(5,3))


def repaso (*agregar):
    for agregacion in agregar:
        print(agregacion.upper())

repaso ={"Armando":"Karina","Flor":"Mima"}
print(repaso)

def cambio (*cambiar):
    for negocio in cambiar:
        print(negocio.upper())

cambio("asus","hp","dell","lenovo","huawei","samsung","apple")

def movile (movil1,movil2,movil3,movil4,movil5 = "sin registrar"):
    print(f"{movil1} {movil2} {movil3} {movil4} {movil5}")

movile(movil1 = "redmi",movil2 ="samsung",movil3 ="huawei",movil4="poco3")

movil = ("redmi","samsung","huawei","poco3")

for cel in movil:
    print(cel.upper())
    if cel == "poco3":
        break
else:
    print("se detiene la variable movile")    

print("la variable se detuvo")
    
import math

def cateto1 (hipotenusa,cateto2):
    return math.sqrt(hipotenusa**2 - cateto2**2)

print("El cateto es igual a",cateto1(5,4))

def pacarni_plata (distancia,velocidad):
    return distancia / velocidad * 100

print("El tiempo que demora en llegar a la plta es",pacarni_plata(46,70))

import math

def area_t (cate1,cate2):
    return math.sqrt(cate1**2 + cate2**2)

print(f"el hipotenusa es",area_t(4,5))


base = int(input("Ingrese su base:"))
altura = int(input("Ingrese su altura:"))
resultado = base * altura / 2
print("El resultado es:",resultado)

# de esta menera se puede hacer desde el terminal

import math

cateto_1 = int(input("Ingrese cateto 1: "))
cateto_2 = int(input("Ingrese cateto 2: "))
my_hipotenusa = math.sqrt(cateto_1**2 + cateto_2**2)
print("El resultado de la hipotenusa es: ",my_hipotenusa)


#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")