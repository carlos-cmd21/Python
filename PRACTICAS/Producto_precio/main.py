from config import ARCHIVOPRODUCTO
def buscar_producto():
    with open(ARCHIVOPRODUCTO,"r",encoding="UTF-8") as archivo:
        contenido = archivo.readlines()
        if contenido:
            producto=input("Ingrese producto :")
            encontrado = False
            for linea in contenido:
                nombre,precio =linea.strip().split(",")
                if nombre.lower() == producto.lower():
                    print(f"El producto {nombre} tiene un valor de {precio}")
                    encontrado = True
                    break
    
            if not encontrado:
                print("El producto no existe")  
        else:
            print("No hay productos para consultar")


buscar_producto()


# ## Version Chatgpt
# from config import ARCHIVOPRODUCTO

# def buscar_producto():
#     with open(ARCHIVOPRODUCTO, "r", encoding="UTF-8") as archivo:
#         contenido = archivo.readlines()

#         if not contenido:
#             print("No hay productos para consultar")
#             return

#         producto = input("Ingrese producto: ")

#         encontrado = False

#         for linea in contenido:
#             nombre, precio = linea.strip().split(",")

#             if nombre.lower() == producto.lower():
#                 print(f"El producto {nombre} tiene un valor de {precio}")
#                 encontrado = True
#                 break

#         if not encontrado:
#             print("El producto no existe")

# buscar_producto()
  
