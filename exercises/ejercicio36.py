import random

opciones = ["piedra", "papel", "tijera"]

print("Bienvenido a 'Piedra, Papel o Tijera'")

while True:
    opcion = input("\nElige piedra/papel/tijera o escribe 'salir': ").lower()

    if opcion == "salir":
        print("Gracias por jugar 👋")
        break

    if opcion not in opciones:
        print("Selección inválida, intenta de nuevo.")
        continue

    usuario = opciones.index(opcion)
    computadora = random.randint(0, 2)

    print(f"Tú: {opciones[usuario]} | CPU: {opciones[computadora]}")

    resultado = (usuario - computadora) % 3

    if resultado == 0:
        print("¡Empate!")
    elif resultado == 1:
        print("¡Ganaste!")
    else:
        print("Perdiste :(")
        