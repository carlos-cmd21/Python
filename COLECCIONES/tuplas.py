#Tuplas colección ordenada e inmutable de elementos que permiten duplicados
#Se definen con paréntesis ()
tecnologias=("Python","Javascript","Go")
print(tecnologias)
print(tecnologias[1]) #Acceder a un elemento por su índice
print(len(tecnologias)) #Obtener la longitud de la tupla
print(type(tecnologias)) #Verificar el tipo de dato
frutas=("manzana",)
print(type(frutas)) #Esto no es una tupla, es un string para indicar que sea una tupla toca poner la coma
Tupla = ("Python",1,True)
print(type(Tupla)) #Tupla con diferentes tipos de datos
x,y,z=Tupla #Desempaquetado de tupla
print(x) #Python
print(y) #1
print(z) #True

tupla1=(1,2,3)
tupla2=(3,4,5)
tupla3=tupla1+tupla2 #Concatenación de tuplas
print(tupla3) #(1, 2, 3, 3, 4, 5)
Tupla = ("Python",1,True)
print(Tupla*2) #Repetición de tupla
for item in Tupla:
    print(item) #Iterar sobre los elementos de la tupla
print("-------------")
tuplaAmodificar=("Python","Javascript","Go")
listacomodin=list(tuplaAmodificar) #Convertir tupla a lista para modificarla
listacomodin.append("ReactJS") #Agregar un nuevo elemento a la lista
tuplaAmodificar=tuple(listacomodin) #Convertir la lista de nuevo a tupla
print(tuplaAmodificar) #('Python', 'Javascript', 'Go', 'ReactJS')