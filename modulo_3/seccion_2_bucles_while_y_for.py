import time

'''
Ejercicio 1: ADIVINA EL NÚMERO SECRETO.

Escenario
Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

- pedirá al usuario que ingrese un número entero;
- utilizará un bucle while;
- comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."
'''

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

user_number = int(input("Que numero es el que esconde el mago: "))

while user_number != secret_number:
    print("¡Ja, ja! ¡Estas atrapado en mi bucle!")
    user_number = int(input("Que numero es el que esconde el mago: "))

print("¡Bien hecho, muggle! Eres libre ahora")

#/--------------------------------------------------------------------------------------------------------------------------------/

'''
Ejercicio 2: FUNDAMENTOS DEL BUCLE FOR- CONTANDO LENTAMENTE (mississippily)

Escenario
¿Sabes lo que es Mississippi? Bueno, es el nombre de uno de los estados y ríos en los Estados Unidos. El río Mississippi tiene aproximadamente 2,340 millas de largo, lo que lo convierte en el segundo río más largo de los Estados Unidos (el más largo es el río Missouri). ¡Es tan largo que una sola gota de agua necesita 90 días para recorrer toda su longitud!

La palabra Mississippi también se usa para un propósito ligeramente diferente: para contar mississippily (mississippimente).

Si no estás familiarizado con la frase, estamos aquí para explicarte lo que significa: se utiliza para contar segundos.

La idea detrás de esto es que agregar la palabra Mississippi a un número al contar los segundos en voz alta hace que suene más cercano al reloj, y por lo tanto "un Mississippi, dos Mississippi, tres Mississippi" tomará aproximadamente unos tres segundos reales de tiempo. A menudo lo usan los niños que juegan al escondite para asegurarse de que el buscador haga un conteo honesto.

Tu tarea es muy simple aquí: escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!"
'''
# Escribe un bucle for que cuente hasta cinco.
for count in range(6):
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    print(f"{count} Mississippi")
    # Cuerpo del bucle, emplea : time.sleep(1)
    time.sleep(1)
    
    # Escribe una función print con el mensaje final.
print("Lista o no, aquí vengo!")


#/--------------------------------------------------------------------------------------------------------------------------------/


'''
Ejercicio 3: LA SENTENCIA BREAK - ATRAPADO EN UN BUCLE

Escenario
La instrucción break se implementa para salir/terminar un bucle.

Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.

No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la sentencia break.
'''

palabra = input("Ingresa una plabara: ")

while True:
    if palabra == 'chupacabra' or palabra == 'Chupacabra' or palabra == 'CHUPACABRA':
        print('Has dejado el bucle con exito!')
        break
    else:
        palabra = input("Ingresa una plabara: ")


#/--------------------------------------------------------------------------------------------------------------------------------/

'''
Ejercicio 4: LA SENTENCIA CONTINUE - EL FEO DEVORADOR DE VOCALES

Escenario
La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.

Se puede usar tanto con bucles while y for.

Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

- un bucle for;
- el concepto de ejecución condicional (if-elif-else).
- la sentencia continue.

Tu programa debe:

- pedir al usuario que ingrese una palabra.
- utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
- utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
- imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada
'''
word_whithout_vowels = ''
# Usuario introduce una palabra
user_word = input("Ingresa una palabra: ")
# Convertimos la palabra en Mayusculas.
user_word = user_word.upper()

for letter in user_word:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue
    else:
        word_whithout_vowels += letter
print(word_whithout_vowels)


#/--------------------------------------------------------------------------------------------------------------------------------/

'''
Ejercicio 5: FUNDAMENTOS DEL BUCLE WHILE.

Escenario
Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
'''

blocks = int(input("Ingresa el número de bloques: "))
height = 0
capa_actual = 1
while blocks >= capa_actual:
    blocks -= capa_actual
    height += 1
    capa_actual += 1


print("la altura de la pirámide.", height)


'''
Ejercicio 6: LA HIPÓTESIS DE COLLATZ.

Escenario
En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
si es par, evalúa un nuevo c0 como c0 ÷ 2;
de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
si c0 ≠ 1, salta al punto 2.
La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

Por supuesto, es una tarea extremadamente compleja usar una computadora para probar la hipótesis de cualquier número natural (incluso puede requerir inteligencia artificial), pero puede usar Python para verificar algunos números individuales. Tal vez incluso encuentres el que refutaría la hipótesis.

Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.

Sugerencia: la parte más importante del problema es como transformar la idea de Collatz en un bucle while- esta es la clave del éxito.
'''

user_number = int(input("Ingresa un numero entero: "))

while user_number <= 0:
    print(user_number)
    print("El numero tiene que ser mayor que cero.")
    user_number = int(input("Ingresa un numero entero: "))

c0 = user_number
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        print(c0)
        steps += 1
    else:
        c0 = 3 * c0 + 1
        steps += 1
        print(c0)

print('Pasos: ', steps)