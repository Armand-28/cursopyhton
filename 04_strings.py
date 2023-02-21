#Strings 

mi_string = " mi string"
mi_otro_string = "mi otro  string"

print( len(mi_string))
print( len(mi_otro_string))

print( mi_string + " " +  mi_otro_string)

mi_new_line_string = "Este es un string\ncon salto de linea"
print(mi_new_line_string)

mi_tab_line_string = "Este es un string con tabulacion\tcon salto de linea"
print(mi_tab_line_string)

mi_scape_string = "\tEste es un string con texto \n escapado"
print(mi_scape_string)

mi_sca_string = "\\tEste es un string con texto \\n escapado" # de esta manera no afecta nada ni el salto de linea  ni la tabulacion
print(mi_sca_string)

#formateo

name, surname, age = "Armando", "Perdomo", 18
print("Mi nombre es: %s  %s tengo: %d " %(name, surname,age) )
print("Mi nombre es: {} {}  tengo: {} " .format(name, surname, age))
print(f"Mi nombre es: {name} {surname} tengo: {age}") # esta es la mejor manera de formatear el codigop ya que es la mas corta y entendible

nombre, apellido, edad = "karina", "Bonilla", 19
print("Mi nombre es: %s %s  tengo: %d " %(nombre, apellido, edad))
print("Mi nombre es: {} {}  tengo: {}" .format(nombre, apellido, edad))
print(f"Mi nombre es: {nombre} {apellido} tengo: {edad}")

name, surname, age, peso = "Armando", "perdomo", 18, 75
print(f"Mi nombre es: {name} mi apellido es: {surname} mi edad es: {age} mi peso es:{peso}")

name, sport, age, torneo = "yeison","natación",35, "chanspions"
print(f"mi nombre es:{name}\n mi deporte favorito es:{sport}\n mi edad es:{age}\n segundo torneo de:{torneo}")

#desempacado de caracteres
lenguage = "python" #ejemplo python tiene 6 caracteres
a, b, c, d, e, f = lenguage   # las variables a  las que igualemos deben ser igual al numero de carracteres entonces debemos llmar 5 letras contando el cero
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

caracteres = "hola"
a, b, c, d = caracteres
print(a, b, c, d)

caracte = caracteres[0:2]
print(caracte)

# Dividsión

language_div = lenguage[1:3]
print(language_div)

language_div = lenguage[1:]
print(language_div)

language_div = lenguage[-4]
print(language_div)

# Reverse

reversed_language = lenguage[::-1]
print(reversed_language)

# Funciones del sistema 

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("n"))
print("1".isnumeric())
print(lenguage.lower())
print(lenguage.upper().isupper())
print(lenguage.lower().islower())
print(lenguage.startswith("py"))


name,edad,rh,cc = "Armando",18, "o+", 1079408351
print(f"Mi nombre es:{name}\nMi edad es:{edad}\nMi tipo de sangre es:{rh}\nMi cedula es:{cc}")
print(name.upper())

name, age, google, opera = "Armando","20", "Google", "Opera"
print(f"Mi nombre es:{name}\n Mi edad es:{age}\nMi navegador favorito es:{google}\nMi segundo navegador favorito es:{opera}")


aquel = "motel"
aa,bb,cc,dd,ee = aquel
print(aa)
print(bb)
print(cc)
print(dd)
print(ee)

where = aquel[0:3]
print(where)

where = aquel[1:4]
print(where)

where = aquel[::-3]
print(where)

play1,play2,play3 = "juan","diego","esteban"
print(f"El jugador uno se llama {play3}\nEl jugador dos se llama {play1}\nEl jugador tres se llama {play1}")