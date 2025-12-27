# Ordenamiento Burbuja

my_list = [8, 10, 6, 2, 4]
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# Ordenamiento Burbuja interactvo

my_list2 = []
swapped = True
num = int(input("Cuantos elementos qieres ordenar: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list2.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list2) - 1):
        if my_list2[i] > my_list2[i + 1]:
            swapped = True
            my_list2[i], my_list2[i + 1] = my_list2[i + 1], my_list2[i]

print("\nOrdenada: ")
print(my_list2)


# Ordenamiento con el metodo '.sort'

my_list3 = [8, 10, 6, 2, 4]

my_list3.sort()
print(my_list3)


# Invertir la Lista con el metodo '.reverse'

my_list3.reverse()
print(my_list3)