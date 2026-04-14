import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


lista_palabras = ["amarillo", "rojo", "violeta", "oliver"]
palabra_elegida = random.choice(lista_palabras)

print("Bienvenido al juego del 'ahorcado'!")
print("\nAdivina la siguiente palabra: \n")

display = []
for _ in palabra_elegida:
    display.append("_")

print(" ".join(display))

vidas = 7
letras_usadas = []
vidas_usadas = -1

while vidas > 0:
    letra_usuario = input("\nIngrese una letra: ").lower()

    # validar que sea una sola letra
    if len(letra_usuario) != 1:
        print("Ingresa solo una letra")
        continue

    # evitar letras repetidas
    if letra_usuario in letras_usadas:
        print("Ya usaste esa letra")
        continue

    letras_usadas.append(letra_usuario)

    if letra_usuario in palabra_elegida:
        for i in range(len(palabra_elegida)):
            if letra_usuario == palabra_elegida[i]:
                display[i] = letra_usuario

        print(" ".join(display))

        # condición de victoria
        if "_" not in display:
            print("\nGanaste 🔥")
            break
    else:
        vidas -= 1
        vidas_usadas +=1
        print(f"\nIncorrecto. Te quedan {vidas} vidas")
        print(HANGMANPICS[vidas_usadas])

# condición de derrota
if vidas == 0:
    print("\nPerdiste 😵")
    print(f"La palabra era: {palabra_elegida}")