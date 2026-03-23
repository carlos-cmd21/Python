x=5
y=3
z=10

if x>y or x>z:
    print("x es mayor que y o x es mayor que z")
elif x==y:
    print("x es igual a y")
else:
    print("ninguna de las condiciones anteriores se cumple")


a="Python"
b="Javascript"
c="Python"

if a==c:
    if a==b:
        print("a es igual a c y a es igual a b")
    else:
        print("a es igual a c pero a no es igual a b")

else:
    print("a no es igual a c")



e=10
f=10
if e==f:
    #no se que hacer si estas dos variables son iguales
    pass  #nos sirve para ignorar el if hasta que sepamos que hacer con el