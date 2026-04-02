year = int(input("Ingrese un año: "))

residuo = year%4

if residuo == 0:
    residuo = year%100
    if residuo == 0:
        residuo = year%400
        if residuo == 0:
            print("leap year")
        else:
            print("Not a leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")
           