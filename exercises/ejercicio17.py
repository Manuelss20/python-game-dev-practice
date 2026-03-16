#trabajamos en un restaurante
#necesitamos un programa que calcule las propinas
#según la cantidad de personas que comieron
#quiero que mi programa le diga a cada persona cuanto es lo que
#tiene que aportar para pagar la cuenta
#el programa tiene que "invitar" a los comensales
#a dejar un 10%, 12%15% de propina
#los comensales pueden decidir que porcentaje de la propina dejar
#hay que mostrar la cuenta total

#primero las entradas
#necesito saber cuantos comensales hay 
comensales=input("dime cuantos comieron")
comensales=int(comensales)
#necesito el total de la cuenta
cuenta=input("de cuanto es la cuenta?")
cuenta=int(cuenta)
#hay que pedir al usuario que indique el porcentaje de propina
#a dejar
propina_usuario=input("dime cuanto de propina vas a dejar, 10%,12%, 15%?")
propina_usuario=int(propina_usuario)

#estructuras de selección------ if, elif, else
if (propina_usuario == 10):
    #calcular la propina
    #en caso de que el usuario haya dejado el 10%
    #cuidar las identaciones
    propina= (cuenta/100)*propina_usuario
    cuenta = cuenta + propina
    
elif (propina_usuario ==12):
    #en caso de que el usuario haya dejado el 12%
    propina = (cuenta/100)*propina_usuario
    cuenta = cuenta + propina

else:
    #en caso de que el usuario haya dejado el 15%
    propina = (cuenta/100)*propina_usuario
    cuenta = cuenta + propina

cuenta_divida=cuenta/comensales
cuenta_divida=round (cuenta_divida, 2)
#hay que mostrar la cuenta total
print (f"la cuenta total es de {cuenta}, incluyendo una propina del {propina_usuario}%")
#tiene que indicar el monto por cada comensal
print (f"dado que comieron {comensales} personas, cada uno debe aportar{cuenta_divida}");
#hay que mostrar la cuenta total