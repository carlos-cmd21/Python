v = True
f= False
print(v)
print(f)
print(5>3) #Verdadero
print(5<3) #Falso
print(type(v)) #Tipo de dato booleano
print(bool("Hola Mundo")) #Cualquier cadena de texto no vacía es verdadera
print(bool("")) #Una cadena de texto vacía es falsa 

#True
print(bool("abc"))
print(bool(123)) 
print(bool(["manzana", "banana", "cereza"]))

#false
print(bool(""))
print(bool(0))      
print(bool([]))
print(bool(None))

x=123
print(isinstance(x,int)) #True

