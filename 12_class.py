##clases##

class mynewpersona:
    pass
print(mynewpersona)
print(mynewpersona())

class persona:
    def __init__(self,name,surname):
        self.nombre_full = f"{name} {surname}"


    def cdath (self):
        print(f"{self.nombre_full} esta estudiando en el sena de la plata huila")


my_persona = persona("Armando","Perdomo")
print(my_persona.nombre_full)
my_persona.cdath()
        
class metas:
    def __init__(self,nombre,apellido,objetivo):
        self.proposito = f"{nombre} {apellido} {objetivo}"

    def nuncat_rindas (self):
        print(f"{self.proposito} nunca te vayas a rendir por que este es mi camino")

sueño = metas("Armando","Perdomo","sera millonario por que este es su deseo 🤑💵💵💵💵💵💵💸💰")
print(sueño.proposito)
sueño.nuncat_rindas()

class comportamineto:
    def __init__(self,habitos,perseverancia,esfuerzo):
        self.granitos = f"{habitos} {perseverancia} {esfuerzo}"

    def malos_habitos(self):
        print(f"{self.granitos} no dejarme ganasr por\n mi malos habitos")

pasos = comportamineto("repetirme mi meta muchas veces en el dia","nunca desistir por fracasos","nunca rendirme por mas dificil que sea")  
print(pasos.granitos)
pasos.malos_habitos()

class motos:
    def __init__(self,discover,pulsar,xtz):
        self.marcas = f"{discover} {pulsar} {xtz}"

    def mas_veloz (self):
        print(f"{marca_motos.marcas} mt09 es la de cilindraje mas veloz se la lleva con 890")    

marca_motos = motos(" discover cilindraje 125"," pulsar cilindraje 180","xtz cilindraje 250")
print(marca_motos.marcas)
marca_motos.mas_veloz()


class animales:
    def __init__(self,dog,cat,cow,rabbit):
        self.animal = f"{dog} {cat} {cow} {rabbit}"

    def especie (self):
        return f"{self.animal} animales de domesticos"

ani = animales("perro","gato","vaca","conejo")
print(ani.animal)
print(ani.especie())

class movil:
    def __init__(self,huawei,redmi,samsung,motorola = "sin nombre"):
        self.moviles = f"{huawei} {redmi} {samsung} ({motorola})"

    def precios (self):
        print(f"{celulares.moviles} todos estos celulares estan en un precio en promedio de 1  de pesos")  # se puiede con la variable nueva quie le damos los datos o con self

celulares = movil("huawei 💵"," redmi 💵","samsumg 💵")
print(celulares.moviles)
celulares.precios()

my_other_cell = movil("huawei 💵"," redmi 💵","samsumg 💵","motorola 💵")
print(my_other_cell.moviles)
my_other_cell.precios()
my_other_cell.moviles = "cristiano ronaldo (cr7)"
print(my_other_cell.moviles)

class carros:
    def __init__(self,car1,car2,car3,car4,car5 = "rapidos"):
        self.autos = f"{car1} {car2} {car3} {car4} ({car5})"

    def carro(self):
        return f"{automoviles.autos} porche es el mas veloz"

automoviles = carros("lamboghini","bmw","renaul","chevrolet")
print(automoviles.autos)
automoviles.carro()


my_other_carros = carros("Bugatti","es","el","carro mas","veloz")
print(my_other_carros.autos)
my_other_carros.carro()
my_other_carros.autos = "El  carro mas rapido de la historia es el (bugatti crithon)"
print(my_other_carros.autos)


class coche:
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def get_marca(self):
        return self.marca

    def encender (self):
        self.encendido = True
        print(f"El coche {self.marca} con modelo {self.modelo} hecho en el año {self.año} ha sido  encendido")

    def apagar (self):
        self.apagado = False
        print(f"El coche {self.marca} con modelo {self.modelo} hecho en el año {self.año} ha sido  apagado")      
    
mi_bmw = coche("bmw 200","x3","2015")
mi_chevrolet = coche("chevrolet","aveo","2004")
#el coche a sido encendido
mi_bmw.encender()
mi_chevrolet.encender()
print(mi_bmw.encendido)
print(mi_chevrolet.encendido)
#el coche a sido apagado
mi_bmw.apagar()
mi_chevrolet.apagar()
print(mi_bmw.apagado)
print(mi_chevrolet.apagado)


class avion:
    def __init__(self,turbinas,aletas,aleron,ruedas):
          self.aviones = f"{turbinas} {aletas} {aleron} {ruedas}"
          self.__ruedas = ruedas
          


    def get_ruedas(self):
        return self.__ruedas #propiedad privada se es privada una clase cuando llleva dos guiones al piso#

    def despegado (self):
        self.despego = True
        print(f"el avion con sus {self.aviones} prendidas a despejado")

    
    def aterrizar (self):
        self.aterrizado = False
        print(f"el avion con sus {self.aviones} a aterrizado")

    def cars (self):
        return f"un carro se compone de {my_carros.aviones}"
        


plane = avion("turbinas","aletas","aleron","ruedas")
print(plane.aviones)
plane.despegado()
print(plane.despego)
plane.aterrizar()
print(plane.aterrizado)
print(plane.get_ruedas())


my_carros = avion("aire","puertas","parabrisas"," y llantas")
print(my_carros.aviones)
print(my_carros.cars())



class ave:

    def __init__(self,tipo,pico,color):
        self.aves_todas = f"{tipo} {pico}{color}"
        self.volando = False

    def volar (self):
        self.volando = True
        print(f"El {aves.aves_todas} esta volando en su pradera")

    def stop (self):
        self.quieto = False
        print(f"El {aves.aves_todas} no esta volando en su pradera")      

    def group (self):
        return f"Estas son las caracteristicas de las aves {aves.aves_todas} todas estas aves  son de partes fresacs"

aves = ave("loro","es de tamaño corto","y de color verde")
print(aves.aves_todas)
print(aves.group())
aves.volar()
print(aves.volando)
aves.stop()
print(aves.quieto)

a = "ooo"

if a in aves.aves_todas:
    print("esta dentro de la clase ave")

elif a == "lo logre":
    print("con practica se puede")

else:
    print("no esta dentro de la variable ave")

class reloj:
    def __init__(self,horas,minutos,segundos):
        self.relojes = f"{horas} {minutos} {segundos}"
        self.marca_hor = False


    def correr (self):
        self.marca_hor = True
        print(f"El reloj esta marcando la hora {tiempo.relojes}")
    
    def detenido (self):
        self.parar = False
        print(f"El reloj esat marcando la hora {tiempo.relojes}")

    def hora_completa (self):
        return f"esta es la hora completa {tiempo.relojes} pm"

tiempo = reloj("⏱️ 3"," minuto 14"," segundo 20")
print(tiempo.relojes)
tiempo.correr()
print(tiempo.marca_hor)
tiempo.detenido()
print(tiempo.parar)
print(tiempo.hora_completa())


class metales:
    def __init__(self,bronce,plata,oro):
        self.bronce = bronce
        self.plata = plata
        self.oro = oro
            
    def medio (self):
        self.bronce = False
        print(f"es mayor el broce que la plata")

    
    def alto (self):
        self.plata = False
        print(f"es mayor la plata que el oro")

    def superior (self):
        self.oro = True
        print(f"es mayor el oro que la plata")

metal = metales("bronce","plata","oro")
print(metal.bronce,metal.plata,metal.oro)
metal.medio()
print(metal.bronce)
metal.alto()
print(metal.plata)
metal.superior()
print(metal.oro)

class rutina:
    def __init__(self,brazo,pierna,abdomen,espalda):
        self.brazo = brazo
        self.pierna = pierna
        self.abdomen = abdomen
        self.esplada = espalda

    def cambios_mes1(self):
        self.mes1 = True
        print(f"Genial trabajar estas partes del cuerpo {rutina_gym.brazo} {rutina_gym.pierna} {rutina_gym.abdomen} {rutina_gym.esplada}")
    
    def mes_12 (self):
        self.mes12 = True
        print(f"haciendo los ejercicios de {self.brazo} {self.pierna} {self.abdomen} {self.esplada} duarante un año estaremos muy acuerpados ")

rutina_gym = rutina("brazo","piernas","abdomen","espalda")
print(rutina_gym.brazo,rutina_gym.pierna,rutina_gym.abdomen,rutina_gym.esplada)
rutina_gym.cambios_mes1()
print(rutina_gym.mes1)
rutina_gym.mes_12()
print(rutina_gym.mes12)


class sena:
    def __init__(self,amb1,amb2,amb3):
        self.amb1 = amb1
        self.amb2 = amb2
        self.amb3 = amb3

    def cargo (self):
        self.horas = "6 horas al dia"
        print(f" Estos programas se trabajan {self.amb1}. {self.amb2}, {self.amb3}.")
    
    def hora (self):
        self.hrs = 1988
        print(f"Estudiando todos los dias {self.amb3} {self.hrs} seremos unos grandes programadores")

clases = sena("construcción","diseño grafico","adso")
print(f" Ambientes del sena: {clases.amb3}, {clases.amb2}, {clases.amb1}.")
clases.cargo()
print(clases.horas)
clases.hora()
print(clases.hrs)
