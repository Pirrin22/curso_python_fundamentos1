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


#/--------------------------------------------------------------------------------------------------------------------------------/


'''
Ejercicio 2: OPERADORES DE COMPARACION Y EJECUCION CONDICIONAL

Escenario
Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o flor de la paz, es una de las plantas para interiores más populares que filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.

Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo, grite involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"

Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.
Prueba tu código con los datos que te proporcionamos. ¡Y hazte de un Espatifilo también!
'''

planta = input('Ingresa el nombre de una planta: ')

if (planta == 'ESPATIFILIO'):
    print('Si - ¡El Espatifilio! es la mejor planta de todos los tiempos!')

elif (planta == 'espatifilo'):
    print('No, ¡quiero un gran Espatifilio!')

else:
    print(f'¡Espatifilio!, ¡No {planta}!')


#/--------------------------------------------------------------------------------------------------------------------------------/

'''
Ejercicio 3: FUNDAMENTOS DE LA SENTENCIA if-else.

Escenario
Érase una vez una tierra de leche y miel - habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto - su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
Tu tarea es escribir una calculadora de impuestos.

Debe aceptar un valor de punto flotante: el ingreso.
A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti - la encontrarás en el código de esqueleto del editor.
Nota: este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.

Observa el código en el editor - solo lee un valor de entrada y genera un resultado, por lo que debes completarlo con algunos cálculos inteligentes.
'''

income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Escribe tu código aquí.
else:
    tax = 14839 + 0.32 * (income - 85528)

if tax < 0.0:
    tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")


#/--------------------------------------------------------------------------------------------------------------------------------/

'''
Ejercicio 4: FUNDAMENTOS DE LA SENTENCIA if-elif-else

Escenario
Como seguramente sabrás, debido a algunas razones astronómicas, el año puede ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

si el número del año no es divisible entre cuatro, es un año común.
de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
de lo contrario, si el número del año no es divisible entre 400, es un año común.
de lo contrario, es un año bisiesto.
Observa el código en el editor - solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.


El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado.

Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.
'''

# Mala praxis
'''
año = int(input("Ingresa el numero del año: "))

if año >= 1582:
    if año % 4 != 0:
        print('Año Común')
    elif año % 100 != 0:
        print("Año Bisiesto")
    elif año % 400 != 0:
        print('Año Común')
    else:
        print('Año Bisiesto')
else:
    print("No dentro del periodo del calendario Gregoriano")
'''
# Buena praxis (compruba lo mismo simplificando el codigo)

año = int(input("Ingresa el numero del año: "))

if año >= 1582:
    if año % 4 != 0 and año % 400 != 0:
        print('Año Común')
    else:
        print('Año Bisiesto')
else:
    print("No dentro del periodo del calendario Gregoriano")