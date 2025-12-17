'''
Ejercicio 1: ENTRADAS SIMPLES Y SALIDAS SIMPLES

Tu tarea es completar el código para evaluar los resultados de cuatro operaciones aritméticas básicas.

Los resultados deben imprimirse en la consola.

Es posible que no puedas proteger el código de un usuario que quiera dividir entre cero. Está bien, no te preocupes por eso por ahora.

Prueba tu código - ¿produce los resultados esperados?

No te mostraremos ningún dato de prueba - eso sería demasiado simple.
'''

# ingresa un valor flotante para la variable a aquí
a = float(input("Ingresa el primer valor: "))

# ingresa un valor flotante para la variable b aquí
b = float(input("Ingresa el segundo valor: "))

# mostrar el resultado de la suma aquí
print(a + b)
# mostrar el resultado de la resta aquí
print(a - b)
# mostrar el resultado de la multiplicación aquí
print(a * b)
# mostrar el resultado de la división aquí
print(round(b / a, 2))

print("\n¡Eso es todo, amigos!")

'''
Ejercicio 2: OPERADORES Y EXPRESIONES

Escenario
Tu tarea es completar el código para poder evaluar la siguiente expresión:

El resultado debe de ser asignado a y. Se cauteloso, observa los operadores y priorízalos. Utiliza cuantos paréntesis sean necesarios.

Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario). Prueba tu código cuidadosamente.
'''

x = float(input("Ingresa el valor para x: "))

# Escribe tu código aquí.

y = 1./(x + 1./(x + 1./(x + 1.)))

print("y =", y)


'''
Ejercicio 2: OPERADORES Y EXPRESIONES 2.

Escenario
La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

No te preocupes si tu código no es perfecto - está bien si acepta una hora invalida - lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.

'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

mins = mins + dura # encontrar el núimero de minutos
hour = hour + mins // 60 # encontrar el número de horas ocultas en los minutos y actualizar horas
mins = mins % 60 # corregir los minutos para que estén en un rango (0..59)
hour = hour % 24 # corregir las horas para que estén en un rango (0..24)


print(hour, ":", mins, sep='')

'''
EJERCICIO.

Calcular hiopotenusa de un triangulo.
'''

anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)

# Este programa calcula la longitud de la hipotenusa

def hipo_triangulo(cateto1, cateto2):
    hipo = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    print('La longitud de la hipotenusa es: ', round(hipo, 3))

cateto1 = float(input('Ingresa la longitud del primer cateto: '))
cateto2 = float(input('Ingresa la longitud del segundo cateto: '))

hipo_triangulo(cateto1, cateto2)