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



