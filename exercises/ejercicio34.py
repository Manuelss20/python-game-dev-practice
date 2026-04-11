#somos unos piratas
#tenemos un tesoro para enterrar
#quiero un programa
#que, pida un numero de dos digitos al usuario
#esos dos digitos son las' coordenadas donde voy a
#enterrar el tesoro
#el programa tiene que pedir las coordenas de donde
#se va a enterrar un tesoro y el programa tiene que
#"enterrar" el tesoro
#hay que mostrar el mapa antes y despues de ocultar
#el tesoro

#primero vamos a representar el mapa

renglon1 = [□, □, □]
renglon2 = [□, □, □]
renglon3 = [□, □, □]

print("el mapa antes de esconder el tesoro luce asi")
print (f"{renglon1} \n{renglon2} \n{renglon3}")
print("nuestro mapa tiene tres columnas y tres renglones")
tesoro = input("en dónde quieres enterrar el tesoro? introduce un número de dos digitos: ")

#necesitamos un ajuste por el contexto
primer_digito=tesoro[0]
primer_digito=int(primer_digito)
 primer_digito-=1
segundo_digito=tesoro[1]
segundo_digito=int(segundo_digito)
segundo_digito-=1

#procedemos a "enterrar" el tesoro"
mapa[primer_digito][segundo_digito]="X"
#falta mostrar el mapa
print (f"{renglon1} \n{renglon2} \n{renglon3}")
