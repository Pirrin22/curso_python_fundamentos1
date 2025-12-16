'''
Ejercicio 1: VARIABLES - PREGUNTAS Y RESPUESTAS.

Escenario
Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100, y True if n es mayor o igual que 100.

No debes crear ningún bloque if (hablaremos de ellos muy pronto). Prueba tu código usando los datos que te proporcionamos.
'''

n = int(input("Ingresa un valor: "))

response = n >= 100
print(response)


#/------------------------------------------------------------------------------------------------------------------------------/
# Usuario introduce 2 numeros.
number1 = int(input("Ingresa el primer numero: "))
number2 = int(input("Ingresa el segundo numero: "))

# Comprobamos cual es el numero mayor.
if number1 > number2:
    largest_number = number1
else:
    largest_number = number2

# Imprimimos el resultado.
print("El numero mayor es: ", largest_number)


#/--------------------------------------------------------------------------------------------------------------------------------/
# Usuario introduce 3 numeros
number1 = int(input("Ingresa el primer numero: "))
number2 = int(input("Ingresa el segundo numero: "))
number3 = int(input("Ingresa el tercer numero: "))

# Asumimos que el numero1 es el mayor y lo almacenamos en la variale largest_number.
largest_number = number1

# Comprobamos si numero2 es mayor que largest_number y si es asi lo almacenamos en la variable largest_number.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si numero 3 es mayor que largest_number y si es asi lo almacenamos en la variable largest_number.
if number3 > largest_number:
    largest_number = number3

# Imprimimos el resultado.
print("el numero mas grande es: ", largest_number)




