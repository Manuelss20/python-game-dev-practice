#hagamos un programa que nos pida nuestra edad

edad=input("dime cuantos años tienes")
edad=int (edad)

#calculos para saber cuantos dias, semanas, meses y años nos quedan

#necesitamos saber cuantos años nos quedan
años_restantes = 100 - edad

#calculando los dias
#años de 365 dias
dias = años_restantes * 365


#calculando las semanas
#años de 52 semanas
semanas = años_restantes * 52

#calculando los meses.
#años de 12 meses
meses = años_restantes * 12

#nos tiene que mostrar nuestros dias, semanas, meses y años restantes
#pero en dias, semanas, meses
#vamos a suponer que vamos a vivir 100 años

print(f"hola, te quedan {años_restantes} años, {meses} meses, {semanas}, semanas y {dias} días")