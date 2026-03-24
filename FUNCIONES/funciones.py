#Funcion 
# Esun bloque de codigo que solo se ejecuta cuando lo llamamos 
# Permite modularizar el codigo y reutilizarlo

def mi_funcion():
    print("Hola mundo desde una funcion")

mi_funcion() # Llamada a la funcion

def saludar(nombre,apellido=""):  #Argumentos
    print(f"Hola {nombre} {apellido}, bienvenido a la programacion")

# saludar("Carlos","Forero")  #Paramentros # Llamada a la funcion con argumento
# saludar("Maria") # Llamada a la funcion con otro argumento

#Argumento se le llama a lo que ponenmos a las variables que esperan una funcion
#Parametros a lo que le pasamos a la funcion 

def sumar (a,b):
    return a + b # Return es lo que devuelve la funcion
sumar(5,10) # Llamada a la funcion con argumentos
resultado = sumar(5,10) # Guardamos el resultado de la funcion en una variable
print(resultado) # Imprimimos el resultado de la funcion

def funcion():
    pass # Pass es una palabra reservada que se utiliza para indicar que no se va a ejecutar nada en esa funcion
