# Variables
mi_variable_string = "Esta es mi primera variable"
print(mi_variable_string)

mi_int_variable = 5
print(mi_int_variable)

mi_int_to_variable = str(mi_int_variable)
print(mi_int_to_variable)
print(type(mi_int_to_variable))

mi_bool_variable = True
print(mi_bool_variable)


#concatenacion de variables en un print
print(mi_variable_string, str(mi_int_variable), mi_bool_variable)

mi_variable_cadena = "esta es una variable con designacion de cadena"
print(mi_variable_cadena)

mi_variable_entero = 10
print(mi_variable_entero)

mi_variable_buleana = False
print(mi_variable_buleana)

mi_variable_con_str = int (mi_variable_buleana)
print (mi_variable_con_str)
print(type(mi_variable_con_str))

#concatenacion de variables en un print que data como resultado tipo de dato "nonetype"
print(type( print(mi_variable_cadena, mi_variable_entero,  int(mi_variable_buleana) )))  

mi_segunda_variable ="esta es una variable de cadena"
print(mi_segunda_variable)

mi_variable_n_entero = 12
print(mi_variable_n_entero)

mi_variable_boleana_2 = True
print(mi_variable_boleana_2)

mi_bool_variable_2 = str (mi_segunda_variable)
print(mi_bool_variable_2)
print(type(mi_bool_variable_2))

print(str(mi_segunda_variable), mi_variable_n_entero, mi_variable_boleana_2)
print("este es el valor de:",mi_variable_boleana_2)


#Funciones del sistema
print(len(mi_segunda_variable)) #len funcion que sirve para saber el numero de caracteres que tiene algun texto

#variables en una sola linea
nombre, apellidos, apodo, edad = "Armando", "perdomo pinacue", "arman", "18 años"
print("mi nombre es:",nombre, "mis apellidos son:",apellidos, "mi apodo es:",apodo,"tengo:", edad)

jugador, numero, antiguedad = "cristiano", 7, "10 años  en los campeonatos"
print("uno de los mas grandes de la historia:",jugador,".se identifica con el numero:",numero,".lleva unos:",antiguedad)

name, sport, experiencia, age = "yeison", "natación", "5 años", 30
print("Mi nombre es:",name,"Mi deporte es:",sport,"Llevo de experiencia:",experiencia,"Mi edad es",age)
 # input ejercicios en la terminal
"""
nombre = input(" ¿cual es tu nombre?")
edad = input("¿cual es tu edad?:")

print(nombre)
print(edad)
"""
#cambia su tipo de dato
nombre = 35
edad = "Esteban"

print(nombre)
print(edad)

# Forzamos el tipo 
address:str = "mi dirección es "
address = 32
print(address)
print(type(address))

my_var = "cadena"
print(my_var)

my_in = 35
print(my_in)

my_bol = True
print(my_bol)

my_bo_in = int(my_bol)
print(my_bo_in)
print(type(my_bo_in))

print(my_var, my_in, int(my_bol))

name,surname = "armando","perdomo"
print(f"mi nombre es: {name}\nmi apellido es: {surname}")


