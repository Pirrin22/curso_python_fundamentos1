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