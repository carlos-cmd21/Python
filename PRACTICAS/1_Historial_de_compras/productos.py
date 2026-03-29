from config import ARCHIVOSPRODUCTOS

def agregar_producto():
    producto = input("Escribe el nombre del producto: ")
    with open(ARCHIVOSPRODUCTOS,"a",encoding="UTF-8") as archivo:
        archivo.write(producto + "\n")
        print("Producto guardado correctamente.")

