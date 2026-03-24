#Diccionarios
#Un diccionario es una colección de datos que se almacenan en pares de clave-valor.
#Los diccionarios se definen utilizando llaves {} y cada par de clave-valor se separa por dos puntos :.
auto ={
    "marca": "Renault",
    "modelo": "Clio",
    "año": 2025,
}
print(auto)
print(auto["marca"])
print(auto.get("marca"))
print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("La marca del auto es una de las propiedades del diccionario")
#cambiar el valor de una clave
auto["año"] = 2020 
print(auto)
#agregar una nueva clave-valor
auto["color"] = "rojo"
print(auto)
auto.update({"año":2022,"puertas":4})
print(auto)

#eliminar elementos
# auto.pop("puertas")
# print(auto)
# auto.popitem() #elimina el ultimo elemento agregado
# print(auto)
# auto.clear() #elimina todos los elementos del diccionario
# print(auto)

for k in auto:
    print(k)
print("----")
for v in auto.values():
    print(v)
print("----")
for k,v in auto.items():
    print(f"{k}: {v}")

#Diccionarios anidados
familia ={
    "hijo1" : {
        "nombre": "Pedro",
        "edad" :8,
    }, 
    "hijo2" : {
        "nombre": "Ana",
        "edad" : 7 ,
    },
    "hijo3" : {
        "nombre": "Marcelo",
        "edad" : 6,
    }
}

print(familia["hijo1"]["nombre"])
