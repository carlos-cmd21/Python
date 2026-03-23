#Las listas son ordenadas,modificables y permiten valores duplicados
#Se escriben entre corchetes []


frutas=["manzana","naranja","mandarina","naranja"]
print(frutas)
print(type(frutas))
frutas[1]="banana"
print(frutas[1])
print(frutas)
lista=["Sergie",1,True]
print(lista)
print(type(lista))
print(len(lista))
print(len(frutas))
print(frutas[0:2])
print(frutas[1:])

if "manzana" in frutas:
    print("La manzana esta dentro de las frutas")

#Metodos
#Append (agregar un elemento al final de la lista)
vehiculos =["Auto","Moto","Bicicleta"]
vehiculos.append("Barco")
print(vehiculos)

#Insert (agregar un elemento en una posicion especifica)
vehiculos.insert(1,"Avion")
print(vehiculos)

#Remove (eliminar un elemento por su valor)
vehiculos.remove("Moto")
print(vehiculos)

#Pop (eliminar un elemento por su indice)
vehiculos.pop(0)
print(vehiculos)

#Sort (ordenar la lista)
vehiculos.sort()
print(vehiculos)

#Reverse (invertir el orden de la lista)
vehiculos.reverse()
print(vehiculos)

#Unir listas
coleccion1=[1,2,3]
coleccion2=[4,5,6]
coleccion3=coleccion1+coleccion2
print(coleccion3)

coleccion1.extend(coleccion2)
print(coleccion1)
