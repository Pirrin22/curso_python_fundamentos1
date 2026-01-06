# Calculadora de IMC (Indice de Masa Corporal).
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2

def lb_to_kg(lb):
    return lb * 0.45359237

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


peso = lb_to_kg(float(input('Ingresa tu peso: ')))
altura = ft_and_inch_to_m(float(input('Ingresa los ft: ')), float(input('Ingresa los inch: ')))

print(bmi(peso, altura))

# Comprobar si tres lados pueden conformar un triangulo.
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        if a > b and a > c:
            return c ** 2 == a ** 2 + b ** 2 
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

lado_a, lado_b, lado_c = float(input('Ingresa el lado a: ')), float(input('Ingresa el lado b: ')), float(input('Ingresa el lado c: '))

if is_a_triangle(lado_a, lado_b, lado_c):
    print('Si, si puede ser un triangulo.')
else:
    print('No, no puede ser un triangulo')

print(is_a_right_triangle(lado_a, lado_b, lado_c))

# Calculado el area de un triangulo reutilizando las funciones anteriores.
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

print(area_of_triangle(lado_a, lado_b, lado_c ** .5))

# Funcion Factorial.
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):
    print(n, factorial_function(n))

# Números Fibonacci

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    the_sum = 0

    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10):
    print(n, '->', fib(n))


