#Operadores de asignacion
x=5
x=x+3 #x ahora es 8
x+=3 #x ahora es 11
x-=3 #x ahora es 8
x-=3 #x ahora es 5
x*=3 #x ahora es 15
x/=3 #x ahora es 5.0
x//=3 #x ahora es 1.0
x%=3 #x ahora es 1
x**=3 #x ahora es 1 
print(x)
y=20
y//=2 #y ahora es 10 y es division entera
y**=3 #y ahora es 1000
print(y)

#Walrus (morsa) := nos permite asignar un valor a una variable como parte de una expresión.
print(z:=3) #z ahora es 3 y se imprime 3        
print(z) #z sigue siendo 3
