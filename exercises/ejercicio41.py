#un programa que pida al usuario un numero entre el 1 y el 1000
#a partir del numero dado que imprima los numeros pares que
#continuan hasta el 1000

numero = int(input("Introduce un número: "))

for i in range(numero,1001):
    if i % 2 == 0:
        print(i)
