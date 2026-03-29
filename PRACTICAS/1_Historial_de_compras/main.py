from menu import menu
from productos import agregar_producto
from historial import ver_historial
from eliminar import eliminarproductos

def main() :
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto() 
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            eliminarproductos()
        elif opcion == "4":
            print("Gracias por utilizar nuestro programa!")
            break
        else:
            print("Seleccione una opción valida")

print(__name__)            
if __name__== "__main__":
    main()