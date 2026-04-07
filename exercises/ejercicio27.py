#quiero un programa que sea una calculadora de amor

#la calculadora de amor funciona de la siguiente manera

#tengo dos nombres, el de "el" y el de "ella"

#me fijo cuantas letras coinciden en los nombres
#con respecto a la frase "true love"

#0+0+1+0+1+0=2
#Marcos
#TRUE LOVE
#Juliana
#0+1+1+0+0+0+0=2

#concatenar de "el" y la suma de "ella"
#"2"+"2"="22"

#el "22" es el puntaje total de compatibilidad

#si el puntaje es menor a 10 o mayor a 90,
#son tan compatibles como la coca cola y los mentos

#si el puntaje está entre 40 y 50, entonces lucen
#compatibles

#en cualquier otro caso los astros no son claros

#hay que pedir datos y hay que convertir a minúsculas
nombre_el = input("Cómo se llama el afortunado?: ")
nombre_el = nombre_el.lower()
nombre_ella = input("Cómo se llama la afortunada?: ")
nombre_ella= nombre_ella.lower()

t = nombre_el.count("t")
r = nombre_el.count("r")
u = nombre_el.count("u")
e = nombre_el.count("e")

l = nombre_el.count("l")
o = nombre_el.count("o")
v = nombre_el.count("v")
e = nombre_el.count("e")

primer_digito = t+r+u+e+l+o+v+e
primer_digito = str(primer_digito)

t = nombre_ella.count("t")
r = nombre_ella.count("r")
u = nombre_ella.count("u")
e = nombre_ella.count("e")

l = nombre_ella.count("l")
o = nombre_ella.count("o")
v = nombre_ella.count("v")
e = nombre_ella.count("e")

segundo_digito = t+r+u+e+l+o+v+e
segundo_digito = str(segundo_digito)

puntaje =  primer_digito + segundo_digito
print (puntaje)
puntaje = int(puntaje)

if(puntaje<10 or puntaje>90):
    print("tan compatibles como la coca cola y mentos") 
elif(puntaje>=40 or puntaje<=50):
    print("Lucen compatibles")
else:
    print ("los astros no son claros al respecto")






