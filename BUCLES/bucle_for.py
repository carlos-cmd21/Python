palabra = "Python"

for letra in palabra:
    print(letra)


adjetivos = ["ricas","Saludabes"]
frutas = ["manzana", "banana", "naranja"]

#Primero hace una vuelta en el for externo y luego en el interno hace 3 vueltas porque son 3 frutas
#luego vuelve al for externo y hace la siguiente vuelta y asi sucesivamente hasta terminar con los adjetivos
for adjetivo in adjetivos:
    for fruta in frutas:
        print(f"{fruta} es {adjetivo}")

for fruta in frutas:
    for adjetivo in adjetivos:
        print(f"{fruta} es {adjetivo}")

for fruta in frutas:
    if fruta == "banana":
        break # Detiene el bucle cuando encuentra "banana"
    print(fruta)

for fruta in frutas:
    if fruta == "banana":
        continue # Salta la iteración cuando encuentra "banana"
    print(fruta)
else: 
    print("El bucle ha terminado sin interrupciones.")


print("---------------------------------")

#Range
#Comienza desde el 0 y termina en el numero que le indiquemos, sin incluirlo
for i in range(10):
    print(i)

# for i in range (1,5):
#     print(i)

for i in range(0,11,2):   # El tercer parametro es el paso, en este caso se salta de 2 en 2
    print(i)    


for i in range(10):
    pass # El pass es una instrucción que no hace nada, se utiliza como un marcador de posición para indicar que no se ha implementado algo aún.