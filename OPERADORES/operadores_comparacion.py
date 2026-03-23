#Operadores de comparación
x=5
y=3
z=5
print(x==y) #False y la comparacion es igual
print(f"{x} es igual a {y}? {x==y}") #False y la comparacion es igual
print(x!=y) #True y la comparacion es distinto
print(f"{x} es distinto a {y}? {x!=y}") #True y la comparacion es distinto
print(x>y) #True y la comparacion es mayor
print(f"{x} es mayor a {y}? {x>y}") #True y la comparacion es mayor
print(x<y) #False y la comparacion es menor
print(f"{x} es menor a {y}? {x<y}") #False y la comparacion es menor
print(x>=z) #True y la comparacion es mayor o igual
print(f"{x} es mayor o igual a {z}? {x>=z}") #True y la comparacion es mayor o igual

#Operadores logicos
x > y and y > z #False y la comparacion es mayor y mayor
print(f"{x} es mayor a {y} y {y} es mayor a {z}? {x > y and y > z}") #False y la comparacion es mayor y mayor
print(x > y and y > z)
print(x > y or y > z)
print(f"{x} es mayor a {y} o {y} es mayor a {z}? {x > y or y > z}") #True y la comparacion es mayor o mayor
v=True
print(not v) #False y la comparacion es negacion
print(f"El valor de v es {v} y su negacion es {not v}") #El valor de v es True y su negacion es False