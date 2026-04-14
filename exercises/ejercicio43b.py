import random

lista_palabras = ["amarillo", "rojo", "violeta"]

palabra_elegida = random.choice(lista_palabras)

print("Bienvenido al juego del 'ahorcado'! - Tienes 4 vidas")
print("\nAdivina la siguiente palabra: \n")

display = []
for i in palabra_elegida:
    display.append("_")

print(" ".join(display))

errores = 0
aciertos = 0
vidas = 4

while errores < 4 and aciertos < len(palabra_elegida):
    letra_usuario = input("\nIngrese una letra: ").lower()
    
    
    if letra_usuario in palabra_elegida:
        for i in range(len(palabra_elegida)):
            if letra_usuario == palabra_elegida[i]:
                aciertos += 1
                display[i] = letra_usuario
                print(" ".join(display))
    else:
        vidas -= 1
        print(f"\nLo sentimos, la letra no es parte de la palabra. Te quedan {vidas} vidas")
        errores += 1
        

if errores == 4:
    print("\nPerdiste!")
else:
    print("\nGanaste!")
        

    
   


            
            
            
            
            
            