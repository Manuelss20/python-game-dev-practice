#tengamos un programa que dado un numero a y un numero b
#podamos invertir las variables de tal modo que
#cuando inicie el algoritmo a=6 , b=8 y cuando termine
#el algoritmo
#las variables estén invertidas a=8 b=6

#definamos la variable a
a=6
#definamos la variable b
b=8

#mostrar valores originales
print("Valores originales")
print("a = ",a)
print("b = ",b)

#invertimos
#crear una variable auxiliar que nos apoye a invertir
c=a
#c=6

#invertimos a
a=b
#a=8

#falta invertir b
b=c
#b=6

#mostremos
print("Valores invertidos")
print("a = ",a)
print("b = ",b)
