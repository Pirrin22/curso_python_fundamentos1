
# Utilizando una lista como argumento de la funcion.
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

'''
Ejercicio 1: UN AÑO BISIESTO: ESCRIBIENDO TUS PROPIAS FUNCIONES.

Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.

La semilla de la función ya se muestra en el código esqueleto del editor.

Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.

El código utiliza dos listas - una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.
'''
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


