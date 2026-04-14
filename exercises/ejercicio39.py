#hagamos programa que saaque el promedio de estaturas
#de un grupo dado

#definamos la lista
altura_estudiantes=[1.50,1.68,1.75,1.90,1.69]
suma = 0
for estudiante in altura_estudiantes:
    suma += estudiante
    
promedio = suma/len(altura_estudiantes)
print(f"el promedio es {promedio}")