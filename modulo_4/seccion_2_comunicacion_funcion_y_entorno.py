# Funciones con un parametro
def message(number):
    print('Ingresa un numero: ', number)

message(1)

# Funcion con dos parametros
def message_2(what, number):
    print(f'Ingresa {what} numero {number}')


message_2('Telefono', 11)
message_2('Precio', 5)
message_2('Numero', 'number')

# Funcion con parametros posicionales

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

def introduction(first_name, last_name):
    print(f'Hola, mi nombre es {first_name} {last_name}')

introduction('Luke', 'Skywalker')
introduction('Jese', 'Quick')
introduction('Clark', 'Kent')

# Funcion con parametros posicionales y le pasamos los argumentos con palabras clave

def introduction(first_name, last_name):
    print(f'Hola, mi nombre es {first_name} {last_name}')

introduction(first_name = 'James', last_name = 'Bond')
introduction(last_name = 'Skywalker', first_name = 'Luke')