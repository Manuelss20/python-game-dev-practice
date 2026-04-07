nombre_el = input("Cómo se llama el afortunado?: ")
nombre_ella = input("Cómo se llama la afortunada?: ")

nombre_el = nombre_el.lower()
nombre_ella = nombre_ella.lower()

contador_el = 0
contador_ella = 0


for i in nombre_el:
    if i in "truelove":
        contador_el +=1
        


for i in nombre_ella:
    if i in "truelove":
        contador_ella +=1
        


puntaje = str(contador_el) + str(contador_ella)

print("El puntaje es: ", puntaje)