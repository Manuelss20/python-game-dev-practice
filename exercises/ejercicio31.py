#el concepto de las listas

#una lista es una agrupación de elementos ordenados
#esperariamos que los datos sean todos del mismo tipo

#si listamos frutas
#manzana, pera, sandia...

#podemos agruparlos mediante una lista

numeros=[10,9,8,7,6,5, 4, 3, 2, 1]
#      =[0,1,2,3, 4,5,6,7,8, n]
#        -------------------->
print (numeros [6])

asistentes=["Ana", "Hilda", "Jose", "Marcos"]
print(asistentes [2])

frutas=[]
print(frutas)

frutas.append("Sandia")
print (frutas)

frutas.append( "Platano")
print (frutas)

fruta=input("que fruta quieres añadir a la canasta")
frutas.append(fruta)
print(frutas)