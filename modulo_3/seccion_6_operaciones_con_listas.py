# Rebanadas en las listas

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


# Rebanada con indice negativo

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# Encontrar el numero mas alto de una lista.

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)


# Encontrar un elemento de la lista.

my_list = list(range(1, 100))
to_find = int(input("Que valor quieres buscar entre el 1 y el 100: "))
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print(f"Elemento encontrado en el indice: {i}")
else:
    print("Ausente")

#------------------------------------------------------------------------------------------------------------------------/

'''
Ejercicio 1: OPERACIONES CON LISTAS:CONCEPTOS BÁSICOS.

Escenario
Imagina una lista - no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros. Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.

Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

Nota: Asume que la lista original está ya dentro del código - no tienes que ingresarla desde el teclado. Por supuesto, puedes mejorar el código y agregar una parte que pueda llevar a cabo una conversación con el usuario y obtener todos los datos.

Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal - no necesitas actualizar la lista actual.
'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_new_list = []
for i in range(len(my_list)):
    if my_list[i] in my_new_list:
        continue
    else:
        my_new_list.append(my_list[i])

print(my_new_list)