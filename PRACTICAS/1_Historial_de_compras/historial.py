from config import ARCHIVOSPRODUCTOS
def ver_historial():
    try:
        with open(ARCHIVOSPRODUCTOS,"r",encoding="UTF-8") as archivo:
            contenido = archivo.readlines()
            if contenido:
                print("Historial de compras:")
                for i, linea in enumerate(contenido,start=1):
                    print(f"{i}. {linea.strip()}")
            else:
                print("El historial está vacio")
    except FileNotFoundError:
        print("No hay ningún producto en el historial.")



# def ver_historial():
#     try:
#         print("Historial de compras:")
#         with open(ARCHIVOSPRODUCTOS,"r",encoding="UTF-8") as archivo:
#             contenido=archivo.read()
#             if contenido:
#                 print(contenido)
#             else:
#                 print("El historial está vacio")
#     except FileNotFoundError:
#         print("No hay ningún producto en el historial.")