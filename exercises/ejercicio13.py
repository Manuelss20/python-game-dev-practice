numero = input("dame un numero de dos digitos")

# quiero sacar el primer digito de ese numero
numero_digito_1 = numero[0]
numero_digito_1 = int(numero_digito_1)
print(type(numero_digito_1))

# quiero sacar el segundo digito de ese numero
numero_digito_2 = numero[1]
numero_digito_2 = int(numero_digito_2)
print(type(numero_digito_2))

# quiero sumar esos digitos
suma = numero_digito_1 + numero_digito_2

print(suma)