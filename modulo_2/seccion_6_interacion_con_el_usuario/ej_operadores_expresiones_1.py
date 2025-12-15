'''
Ejercicio 2: OPERADORES Y EXPRESIONES

Escenario
Tu tarea es completar el código para poder evaluar la siguiente expresión:

El resultado debe de ser asignado a y. Se cauteloso, observa los operadores y priorízalos. Utiliza cuantos paréntesis sean necesarios.

Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario). Prueba tu código cuidadosamente.
'''

x = float(input("Ingresa el valor para x: "))

# Escribe tu código aquí.

y = 1./(x + 1./(x + 1./(x + 1.)))

print("y =", y)
