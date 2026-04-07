#la implementación del modulo random

import random

#generando numeros enteros
#vamos a decir, que necesito "crear", "generar" un numero
#aleatorio entre el 1 y el 10)

numero_aleatorio=random.randint(1,10)
print (numero_aleatorio)

#generando numeros decimales
#random.random------0.00000000-0.99999999
aleatorio_flotante=random.random()
print (aleatorio_flotante)

#vamos a decir, que necesito "crear", "generar" un numero
#aleatorio entre el 0.0 y 4.99999)