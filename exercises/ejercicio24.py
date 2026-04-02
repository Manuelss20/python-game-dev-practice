#somos una pizzeria
#vendemos 3 tipos de pizzas #pequeña, mediana y grande
#pequeña, 15, mediana 20, y la grande 25

#hay que preguntarle al usuario si quiere su pizza con pepperoni
#o no, si quiere pepperoni el costo es de 2

#hay que preguntarle al usuario si quiere extra queso
#si quiere extra queso el costo suma 1

#hay que mostrarle al usuario el total a pagar

tamaño = input("De qué tamaño desea su pizza?(pequeña/mediana/grande) ")
if tamaño == "pequeña":
    total = 15
elif tamaño == "mediana":
    total = 20
elif tamaño == "grande":
    total = 25
else:
    print("tamaño incorrecto")

pepperoni = input("Desea pepperoni?:(si/no) ")
if pepperoni == "si":
    total = total + 2
elif pepperoni == "no":
    total = total
else:
    print("opción incorrecta")

queso = input("Gusta queso?(si/no) ")
if queso == "si":
    total = total + 1
elif queso == "no":
    total = total
else:
    print("opción incorrecta")
    
print ("el total es ", total)
              