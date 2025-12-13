
'''
CONVERSION DE TIPOS DE VARIABLES.
'''

# Los inputs siempre son cadenas de texto, no nos dejaran hacer operaciones matematicas a no se que cambiemos la variable que almacena cadena de texto a una variable que almacene un float o un int.

# Ejemplo 1, este codigo da error. Descomentalo para ve rel resultado del error.
'''
anything = input("Ingresa un número:")
something = anything ** 2.0
print(anything, "al cuadrado es", something)
'''
# Ejemplo 2: este codigo nos da la operacion bien.

anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)

# Este programa calcula la longitud de la hipotenusa

def hipo_triangulo(cateto1, cateto2):
    hipo = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    print('La longitud de la hipotenusa es: ', round(hipo, 3))

cateto1 = float(input('Ingresa la longitud del primer cateto: '))
cateto2 = float(input('Ingresa la longitud del segundo cateto: '))

hipo_triangulo(cateto1, cateto2)