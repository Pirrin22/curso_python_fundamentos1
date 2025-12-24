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