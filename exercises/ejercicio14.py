# vamos a hacer un programa que nos muestra el indice de masa corporal
# corporal

# investigar / saber como se saca el IMC

print("Hola, este es un programa que calcula el IMC")

# necesitamos pedirle al usuario que nos de el peso y su estatura
peso = input("Dame tu peso en kilos")
peso = int(peso)
estatura = input("Dame tu estatura")
estatura = float(estatura)

# necesito dividir el peso entre la estatura elevada al cuadrado
IMC = (peso / (estatura**2))  # operadores aritmetico ---- int-float

# necesito redondear el numero
IMC = round(IMC,1)

# salida, imprimir el IMC
print("Después de calcular, tu IMC es de", IMC)