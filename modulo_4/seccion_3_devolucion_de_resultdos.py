
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



'''
Ejercicio 2: CUANTOS DIAS: ESCRIBIENDO Y USANDO TUS PROPIAS FUNCIONES.

Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.3.1.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función - este truco acortará significativamente el código.
'''
# Revisamos si el año es bisiesto o no.
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return True

def days_in_month(year, month):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1582:
        return None
    elif month < 1 or month > 12:
        return None
    else:
        if month == 2 and is_year_leap(year):
            return 29
        return dias_por_mes[month - 1]
    
    

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


'''
Ejercicio 3: DIA DEL AÑO: ESCRIBIENDO Y USANDO TUS PROPIAS FUNCIONES.

Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.
'''
# Comprobamos si un año es bisiesto
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return True
    

# Comprobamos los dias del mes/año
def days_in_month(year, month):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1582:
        return None
    elif month < 1 or month > 12:
        return None
    else:
        if month == 2 and is_year_leap(year):
            return 29
        return dias_por_mes[month - 1]
    

def day_of_year(year, month, day):
    dias_mes_totales = days_in_month(year, month)
    if dias_mes_totales == None:
        return None
    if day < 1 or day > dias_mes_totales:
        return None
    
    resultado = day

    for i in range(1, month):
        resultado = resultado + days_in_month(year, i)
    return resultado

print(day_of_year(2000, 12, 31))
print(day_of_year(2023, 1, 1))
print(day_of_year(2023, 3, 1))
print(day_of_year(2023, 2, 30))
