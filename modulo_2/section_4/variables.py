'''
Ejercicio de Variables 1:
A continuación una historia:

Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

Tu tarea es:

Crear las variables: john, mary, y adam;
Asignar valores a las variables. El valor debe de ser igual al número de manzanas que cada quien tenía;
Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma;
Después se debe crear una nueva variable llamada total_apples y se debe igualar a la suma de las tres variables anteriores;
Imprime el valor almacenado en total_apples en la consola;
Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, "Número total de manzanas:" y total_apples.
'''

jhon = 3
mary = 5
adam = 6
print(jhon, mary, adam, sep=",")

total_apples = (jhon + mary + adam)

print(total_apples)

print("Total de manzanas entre los 3:", total_apples)



'''
Ejercicio de variables 2:
Millas y kilómetros son unidades de longitud o distancia.

Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:

Millas a kilómetros;
Kilómetros a millas.
No se debe cambiar el código existente. Escribe tu código en los lugares indicados con ###. Prueba tu programa con los datos que han sido provistos en el código fuente.

Pon mucha atención a lo que esta ocurriendo dentro de la función print(). Analiza como es que se proveen múltiples argumentos para la función, y como es que se muestra el resultado.

Nota que algunos de los argumentos dentro de la función print() son cadenas (por ejemplo, "millas son", y otros son variables (por ejemplo, miles).

Consejo:  
Hay una cosa interesante más que esta ocurriendo. ¿Puedes ver otra función dentro de la función print()? Es la función round(). Su trabajo es redondear la salida del resultado al número de decimales especificados en el paréntesis, y regresar un valor flotante (dentro de la función round() se puede encontrar el nombre de la variable, el nombre, una coma, y el número de decimales que se desean mostrar). Se hablará más de esta función muy pronto, no te preocupes si no todo queda muy claro. Solo se quiere impulsar tu curiosidad.

Después de completar el laboratorio, abre Sandbox, y experimenta más. Intenta escribir diferentes convertidores, por ejemplo, un convertidor de USD a EUR, un convertidor de temperatura, etc. - ¡Deja que tu imaginación vuele! Intenta mostrar los resultados combinando cadenas y variables. Intenta utilizar y experimentar con la función round() para redondear tus resultados a uno, dos o tres decimales. Revisa que es lo que sucede si no se provee un dígito al redondear. Recuerda probar tus programas.

Experimenta, saca tus propias conclusiones, y aprende. Sé curioso.
'''

def change_distace(kilometers, miles):

    miles_to_kilometers = miles * 1.61
    kilometers_to_miles = kilometers / 1.61

    print(miles, "millas son", round(miles_to_kilometers, 2), "kilometros")
    print(kilometers, "kilometros son", round(kilometers_to_miles, 2), "millas")

change_distace(12.25, 7.38)

def change_temperature(celsius, fahrenheit):

    celsius_to_fahrenheit = (celsius * 1.8) + 32
    fahrenheit_to_celsius = (fahrenheit - 32) / 1.8

    print(celsius, "celsius son", round(celsius_to_fahrenheit, 2), "fahrenheit")
    print(fahrenheit, "fahrenheit son", round(fahrenheit_to_celsius, 2), "celsius")

change_temperature(42, 96)


def change_money(usd, eur):

    usd_to_eur = usd * 0.8526
    eur_to_usd = eur / 0.8526

    print(usd, "dolares son", round(usd_to_eur, 2), "euros")
    print(eur, "euros son", round(eur_to_usd, 2), "dolares")

usd = input("ingrasa la cantidad de dolares: ")
eur = input("ingrasa la cantidad de euros: ")
change_money(float(usd), float(eur))