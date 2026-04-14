#hagamos un programa que sea un generador de contraseñas
#este programa debe pedir al usuario
#la cantidad de letras de la contraseña
#la cantidad de numeros
#la cantidad de simbolos a utilizar

# MI VERSIÓN
import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
numeros = ['0','1','2','3','4', '5', '6', '7', '8', '9']

simbolos = ['!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?']

cantidad_letras = int(input("Ingrese la cantidad de letras que desea en su contraseña: "))
cantidad_numeros = int(input("Ingrese la cantidad de numeros que desea en su contraseña: "))
cantidad_simbolos = int(input("Ingrese la cantidad de simbolos que desea en su contraseña: "))

contrasena = []

for i in range(0,cantidad_letras):
    indice_aleatorio = random.randint(0, 25)
    contrasena.append(letras[indice_aleatorio])
    
for i in range(0,cantidad_numeros):
    indice_aleatorio = random.randint(0, 9)
    contrasena.append(numeros[indice_aleatorio])
    
for i in range(0,cantidad_simbolos):
    indice_aleatorio = random.randint(0, 10)
    contrasena.append(simbolos[indice_aleatorio])
    
print(f"Su nueva contraseña es: {''.join(contrasena)}")

# VERSION LIMPIA
import random
import string

cantidad_letras = int(input("Letras: "))
cantidad_numeros = int(input("Números: "))
cantidad_simbolos = int(input("Símbolos: "))

contrasena = []

for _ in range(cantidad_letras):
    contrasena.append(random.choice(string.ascii_letters))

for _ in range(cantidad_numeros):
    contrasena.append(random.choice(string.digits))

for _ in range(cantidad_simbolos):
    contrasena.append(random.choice(string.punctuation))

random.shuffle(contrasena)

print("Contraseña:", ''.join(contrasena))

