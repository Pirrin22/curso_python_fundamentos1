# Creo mi primera funcion.

def message():
    print("Por favor ingresa un valor:")


message()
a = int(input())
message()
b = int(input())
message()
c = int(input())


# Optimizando la funcion anterior:

def message_2():
    return int(input("Por favor ingresa un valor: "))

a = message_2()
b = message_2()
c = message_2()

print(a)
print(b)
print(c)



