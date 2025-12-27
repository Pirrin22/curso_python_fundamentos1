numbers = [10, 5, 7, 2, 1]
print(f"Lista original: {numbers}")

# Asignacion de valor por indexacion.
numbers[0] = 111
print(f"Nuevo contenido de la lista: {numbers}")

# Copiar un elemento de la lista en otro indice de la lista

numbers[1] = numbers[4]
print(f"Nuevo contenido de la lista: {numbers}")

# Saber la longitud de la lista
print(f"La lista contiene {len(numbers)} valores")

# Eliminar valores de una lista
del numbers[1]
print(f"La lista queda asi: {numbers}")
print(f"La nueva longitud de de la lista es de {len(numbers)} valores")

# Se pueden utilizar indices negativos(sireve para correr la lista de derecha a izquierda).
print(f"El ultimo elemento de la lista es: {numbers[-1]}")
print(f"EL penultimo elemento de la lista es: {numbers[-2]}")

'''
Ejercicio 1: LOS FUNDAMENTOS DE LA S LISTAS.

Escenario
Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

Tu tarea es:

- escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
- escribir una línea de código que elimine el último elemento de la lista (Paso 2)
- escribir una línea de código que imprima la longitud de la lista existente (Paso 3).- 
'''

sombrero = [1, 2, 3, 4, 5]

print(f"Lista original de sombrero: {sombrero}")

sombrero[2] = int(input("Ingresa un numero para cambiar el valor del indice 2 de la lista: "))
print(f"La lista actual queda asi: {sombrero}")
del sombrero[4]
print(f"La longitud de la lista es: {len(sombrero)}")

#----------------------------------------------------------------------------------------------------------------#

# Añadir un elemento al final de la lista.
numbers.append(12)
print(f"La lista despues de añadir un elemeto mas: {numbers}")

# Añadir un elemento en el lugar que queramos de la lista.
numbers.insert(3, 15)
print(f"La lista despues de añadir un elemento al indice seleccionado: {numbers}")

# Creamos una lista vacia y la llenamos con un bucle for.
llenar_con_bucle = []

for i in range(5):
    llenar_con_bucle.append(i + 1)

print(f"La lista vacia 'llenar_con_bucle' ahora tiene los siguientes numeros: {llenar_con_bucle}")

# Creamos una lista vacia y la llenamos con un bucle for con inicio en 0.
llenar_con_bucle2 = []

for i in range(5):
    llenar_con_bucle2.insert(0, i + 1)

print(f"La lista vacia 'llenar_con_bucle2' ahora contiene: {llenar_con_bucle2}")

# Sumamos todos los valores de una lista con el bucle for.
sumar_lista = [10, 1, 8, 3, 5]
total = 0

for i in range(len(sumar_lista)):
    total += sumar_lista[i]

print(f"La suma total de los elementos de la lista es: {total}")

sumar_lista2 = [10, 1, 8, 3, 5]
total2 = 0

for i in sumar_lista2:
    total2 += i

print(f"El total de la suma de los elementos de 'sumar_lista2' es: {total2}")

# Cambiar elementos de una lista a otra.

my_list = [10, 1, 8, 3, 5]
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

#----------------------------------------------------------------------------------------------------------------#

'''
Ejercicio 5: LOS FUNDAMENTOS DE LAS LISTAS: LOS BEATLES

- Escenario
Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.

La banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).


Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

- paso 1: crea una lista vacía llamada beatles;
- paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
- paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
- paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
- paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.

'''
# Paso 1: Crea una lista Vacia
beatles = []
print(f"Paso 1: {beatles}")

# Paso 2: Empleo el metodo 'append()' para llenar algunos elementos en la lista.
beatles.append("Jhon Lennon")
beatles.append("Paul McCartbey")
beatles.append("George Harrison")
print(f"Paso 2: {beatles}")

# Paso 3: Empleamos un bucle 'for' para acabar de llenar la lista con el resto de integrantes.

for i in range(2):
    nombre = input(f"Ingresa el nombre de los integrantes que faltan: ")
    beatles.append(nombre)

print(f"Paso 3: {beatles}")

# Paso 4: Usamos la instruccion 'del' para eliminar a los ultimos integrantes de la banda.

del beatles[4]
del beatles[3]

print(f"Paso 4: {beatles}")

# Paso 5: Usamos el metodo 'insert()' para añadir a Ringo Starr al principio de la lista.

beatles.insert(0, 'Ringo Starr')

print(f"Paso 5: {beatles}")