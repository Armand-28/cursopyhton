
# while True:
#     print("Operaciones disponibles: ")
#     print("1. Suma")
#     print("2. Resta")
#     print("3. Multiplicación")
#     print("4. División")
#     print("5. Salir")

#     opcion = int(input("Seleccione una opción (1-5): "))

#     if opcion == 5:
#         break

#     num1 = float(input("Ingrese el primer número: "))
#     num2 = float(input("Ingrese el segundo número: "))

#     if opcion == 1:
#         resultado = num1 + num2
#         print("El resultado de la suma es:", resultado)
#     elif opcion == 2:
#         resultado = num1 - num2
#         print("El resultado de la resta es:", resultado)
#     elif opcion == 3:
#         resultado = num1 * num2
#         print("El resultado de la multiplicación es:", resultado)
#     elif opcion == 4:
#         resultado = num1 / num2
#         print("El resultado de la división es:", resultado)
#     else:
#         print("Opción inválida")
#         if opcion == 5:
#             opcion = opcion+1
#         if opcion != 5:
#             print("Realizar mas operaciones")
#             print(" ")
#             print("5. Si")
#             print("1. No")
#             opcion = float(input())


# numero1 = float()
# numero2 = float()
# contador = float()
# operacion = float()
# contador = 0
# while contador == 0:
#         print("¿Que operación desea realizar?➕")
#         print(" ")
#         print("[1] Suma")
#         print("[2] Resta")
#         print("[3] Multiplicacion")
#         print("[4] División")
#         print("[0] Regresar")
#         contador = float(input())
#         if contador == 1:
#             print("Digite el Primer número")
#             numero1 = float(input())
#             print("Digite el segundo número")
#             numero2 = float(input())
#             operacion = (numero1 + numero2)
#             print("Elresultado de la suma es: ",operacion)
#         else:
#             if contador == 2:
#                 print("Digite el primer número")
#                 numero1 = float(input())
#                 print("Digite el segundo número")
#                 numero2 = float(input())
#                 operacion = (numero1 - numero2)
#                 print("El resultado de la resta es: ",operacion)
#             else:
#                 if contador == 3:
#                     print("Digite el primer número")
#                     numero1 = float(input())
#                     print("Digite el segundo número")
#                     numero2 = float(input())
#                     operacion = (numero1 * numero2)
#                     print("El resultado de la multiplicacion es: ",operacion)
#                 else:
#                     if contador == 4:
#                         print("Digite el primer número")
#                         numero1 = float(input())
#                         print("Digite el segundo número")
#                         numero2 = float(input())
#                         operacion = (numero1 / numero2)
#                         print("El resultado de la División es: ",operacion)
#                     else:
#                         if contador == 0:
#                             contador = contador+1
#         if contador != 0:
#             print("Desea realizar mas operaciones💵")
#             print(" ")
#             print("[0] Si")
#             print("[1] No")
#             contador = float(input())

while True:
    print("Seleccione una operación")
    print("[1] Suma")
    print("[2] Resta")
    print("[3] Multiplicación")
    print("[4] División")
    print("[5] Salir")
    print(" ")
    selecio = int(input("Seleccione la operacion que desea realizar:"))

    if selecio == 5:
        break

    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    if selecio == 1:
        resultado = numero1 + numero2
        print("El resultado sde la suma es: ",resultado)
    elif selecio == 2:
        resultado = numero1 - numero2
        print("El resultado de la resta es:",resultado)
    elif selecio == 3:
        resultado = numero1 * numero2
        print("El resultado de la multiplicación es: ",resultado)
    elif selecio == 4:
        resultado = numero1 / numero2
        print("El resultadoi de la división es: ",resultado)
    else:
        print("Selecion invalida")
        break
    
    

        
        
    
           