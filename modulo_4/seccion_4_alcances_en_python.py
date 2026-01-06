# Variable fuera de la funcion, pero al definir la variable antes de llamar a la funcion, la funcion la reconoce
def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)


# La misma variable definida dentro y fuera de la funcion, la variable de dentro de la funcion no es la misma que la de fuera
def my_function():
    var = 2
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)


# Palabra reservada 'global' hace que la variable no varie.
def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)


# Pasamos un argumento 'lista' y lo modificamos en el interior.
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)





