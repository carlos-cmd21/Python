#Lambda es una funcion pequeña y anonima que puede tener muchos argumentos pero solo una expresion
#Se utiliza para crear funciones pequeñas y de una sola linea, es decir, funciones que no necesitan un bloque de codigo completo
#La sintaxis de una funcion lambda es la siguiente:
#lambda argumentos: expresion
# x=lambda a,b:a+b
# print(x(5,10)) #Salida: 15

def mifuncion(n):
    return lambda a: a * n

duplicador = mifuncion(2)
triplicador = mifuncion(3)

print(duplicador(5)) #Salida: 10
print(triplicador(5)) #Salida: 15