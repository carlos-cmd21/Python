#Conjuntos
#Coleccion no ordenada de elementos unicos (no tiene indice)
from math import e


frutas={"manzana","naranja","mandarina","naranja"} #Los elementos duplicados se eliminan automáticamente
print(frutas)
print(type(frutas)) #Verificar el tipo de dato
print(len(frutas)) #Obtener la longitud del conjunto
print("naranja" in frutas) #Verificar si un elemento está en el conjunto
print("pera" not in frutas) #Verificar si un elemento no está en el conjunto

#Agregar elementos a un conjunto
frutas.add("pera") #Agregar un nuevo elemento al conjunto
print(frutas)

#update para agregar varios elementos a un conjunto
#tambien sirve para agregar listas, tuplas
frutastropicales={"piña","mango","papaya"}
frutas.update(frutastropicales) #Agregar los elementos de otro conjunto al conjunto original
frutas.update(["kiwi","fresa"]) #Agregar varios elementos al conjunto

#Eliminar elementos de un conjunto
#remove
frutas.remove("manzana") #Eliminar un elemento del conjunto, si el elemento no existe ***se*** genera un error
print(frutas)
#discard
frutas.discard("naranja") #Eliminar un elemento del conjunto, si el elemento no existe ***no*** se genera un error
print(frutas)
#pop elimina un elemento aleatorio al no tener indice
frutas.pop() #Eliminar un elemento aleatorio del conjunto
print(frutas)
#clear
frutas.clear() #Eliminar todos los elementos del conjunto
print(frutas)

# conjuntos={"Python",123,True} #Conjunto con diferentes tipos de datos
# print(len(conjuntos)) #Obtener la longitud del conjunto 
# print(conjuntos) #El orden de los elementos no es garantizado
# print(type(conjuntos)) #Verificar el tipo de dato

# for item in conjuntos:
#     print(item) #Iterar sobre los elementos del conjunto

print("-----------------------")
#Operaciones con conjuntos
a={"a","b","c"}
b={"c","d","e"} 

c=a.union(b) #Unión de conjuntos
print(c) #{'a', 'b', 'c', 'd', 'e'}
i=a.intersection(b) #Intersección de conjuntos
print(i) #{'c'}
d=a.difference(b) #Diferencia de conjuntos
print(d) #{'a', 'b'}