#supongamos que estamos en un concurso
#hay una lista de participantes
#quiero que la computadora de manera aleatoria
#seleccion a la siguiente persona en irse
#VIc Broda

import random

participantes=["Juan", "Julian", "Sofia", "Amadis" ]
#            =[   0       1         2        3     ]

numero_aleatorio=random.randint(0,3)  # 0, 1, 2, 3
print(numero_aleatorio)

victima = participantes[numero_aleatorio]
print (f"lo sentimos, {victima} se tiene que ir")
