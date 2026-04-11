import random 


print("Bienvenido a \"piedra, papel o tijera\"")
opcion = input("ingresa que opción lanzarás! piedra/papel/tijera: ")

indice_aleatorio =  random.randint(0, 2)
opciones = ["piedra", "papel", "tijera"]
opcion_computadora = opciones[indice_aleatorio]
opcion = opcion.lower()

if opcion == "piedra":
    indice = 0
elif opcion == "papel":
    indice = 1;
elif opcion == "tijera":
    indice = 2;
else:
    print("selección incorrecta, intente de nuevo")
    exit()
    
print(f"Tu selección es: {opcion}.\nLa selección de la computadora es: {opcion_computadora}")

if indice == indice_aleatorio:
    print("¡Empate!")
elif  (indice == 0 and indice_aleatorio == 1) or \
      (indice == 1 and indice_aleatorio == 2) or \
      (indice == 2 and indice_aleatorio == 0):
    print("perdiste :(")
else:
    print("¡Ganaste!")
    

    