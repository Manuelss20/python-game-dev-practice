#hagamos programa que saaque el promedio de estaturas
#de un grupo proporcionado por el usuario
#y vamos a obtener el puntaje máximo

#definamos la lista
#puntaje_estudiantes=[1.50,1.68,1.75,1.90,1.69]

puntaje_estudiantes = []
cantidad_puntajes= int(input("Ingrese la cantidad puntajes a ingresar: "))

i = 0
puntaje = 0

while i < cantidad_puntajes:
    puntaje = int(input(f"Ingrese el puntaje #{i+1}: "))
    puntaje_estudiantes.append(puntaje)
    i += 1              

suma = 0
for puntajes in puntaje_estudiantes:
    suma += puntajes
    
promedio = suma/len(puntaje_estudiantes)
print(puntaje_estudiantes)
print(f"El promedio es: {promedio}")

#calcular el puntaje maximo

maximo = puntaje_estudiantes[0]

for puntaje in puntaje_estudiantes:
    if puntaje > maximo:
        maximo = puntaje
        
print(f"El puntaje máximo es{maximo}")