# pedimos al usuario su nombre
nombre = input("Dime tu primer nombre")  # nombre --- string

# calculamos la longitud del mismo
longitud_nombre = len(nombre)

# vamos a imprimir todo pero concatenado
print("Te llamas", nombre, " y tu nombre tiene", longitud_nombre, " letras")

# recordar que existe type
tipo_nombre = type(nombre)
print(tipo_nombre)
tipo_longitud_nombre = type(longitud_nombre)
print(tipo_longitud_nombre)