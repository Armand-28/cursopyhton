##excepciones handling##

num1 = 10
num2 = 8
num2 = "8"

#  try except
try:  # simpre que haya un try debe de haber un except
    print(num1 + num2)
    print("No hay errores")

except:
    # se ejecuta si no se produce una excepcion
    print("Error en la suma de variables")

# try except else finally

try:#se ejecuta si es correcta las oepraciones
    print(num1 + num2)
    print("No hay errores")
except:
    print("Errorres en la suma de variables")

# se ejecuta si no se produce una excepcion
else:#opcional
    print("la ejecucion continua correctamente")

finally:#opcional
    # se ejecuta siempre (finally)
    print("La ejecución continua")

a = 4
b = 6
b = "6"

try:
    print(a + b)
    print("No hay errores")
except:
    print("Esta variable contine errores")


try:
    print(a + b)
    print("no hay errores")
except:
    print("Se encuentran errores")
else:
    print("La ejecucion continua corectamente")
finally:
    print("continua pase lo que pase")



# excepciones por tipo
try:
    print(a + b)
    print("No hay errores")

except ValueError:
    print("se ha producido un valueError")

except TypeError:
    print("se ha producido un TypeError")

#Captura de la información de la excepción
try:
    print(a + b)
    print("No hay errores")

except ValueError as error:
    print(error)
except Exception as errores:
    print(errores)





# letter1 = "hola como estas"
# letter2 = "que mas de nuevo compañero"

# print("La variable letras2 tiene: ",len(letter2))

# if letter1 > letter2:
#     print(f"{letter1}\n"* 10)

# else:
#     print("no se cumple la condicion")
    