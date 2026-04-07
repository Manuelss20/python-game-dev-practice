#vamos a programar un volado
#quiero que la computadora de manera aleatoria #lance una moneda y me diga si cae cara o cruz
import random
#generemos el aleatorio

numero_aleatorio=random.random()

if (numero_aleatorio < 0.50):
    print("aguila")
else:
    print("sol")
    
