#vamos a hacer un programa que nos indique, si un numero
#es par, o impar

#módulo es el residuo de una división
#el símbolo del módulo es %

#entradas
numero = input("dime de que numero quieres saber si es par o no")
numero = int(numero)
#proceso
#como le digo a la computadora, si un numero es par o no?
residuo = numero%2

if(residuo==0):
    print("tu número es par")
else:
    print("tu número es impar")
    

