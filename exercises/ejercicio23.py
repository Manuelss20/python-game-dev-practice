#estamos en una montaña rusa #hay un cartel, dice lo siguiente:
#solo usuarios que midan mínimo 120cm pueden
#si tienes menos de 18 años vas a pagar $7
#si tienes mas de 18 pagas $15

#hay que preguntarle al usuario si quiere una foto o no la quiere
#la foto tiene un costo de $3

#necesitamos pedir la estatura al usuario
estatura= input("dime tu estatura")
estatura=int(estatura)
#si tu estatura es mayor a 120 cm puedes pasar
#de lo contrario gg

if(estatura>=120):
    print("diviertete!")
    #primero le pregunto la edad
    edad=input("dime tu edad")
    edad=int (edad)
    #estructura de selección
    if (edad<12):
        precio=3
    elif (edad<18):
        precio=7
    else:
        precio=15
    foto = input("oye, quieres foto?")
    if foto == "si":
        precio_foto = 3
    else:
        precio_foto = 0
    # mostrar el total a pagar
    total = precio + precio_foto
    print(total)
else:
    print("gg")