from config import ARCHIVOSPRODUCTOS
def eliminarproductos():
    try:
        with open(ARCHIVOSPRODUCTOS,"r",encoding="UTF-8") as archivo:
            contenido = archivo.readlines()
            if contenido:
                print("Productos actuales:")
                for i, linea in enumerate(contenido,start=1):
                    print(f"{i}. {linea.strip()}")
                opcion = int(input("Digite el numero a eliminar: "))
                if opcion < 1 or opcion > len(contenido):
                       print("Seleccione una opción valida")
                        
                else: 
                    print(f"Se ha eliminado el siguiente producto: {contenido[opcion - 1].strip()}.")
                    del contenido[opcion - 1]
                    with open(ARCHIVOSPRODUCTOS,"w",encoding="UTF-8") as archivo:
                         archivo.writelines(contenido)
                    
            else: 
                print("No hay productos para eliminar")
    except ValueError:
        print("Debes ingresar un numero válido")

