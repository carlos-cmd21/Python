from menu import mostrar_menu
from pedidos import pedircafe
from historial import ver_historial
def main():
    while True:
        mostrar_menu()
        opcion= input("Selecciona una opcion: ")
        if opcion == "1":
            pedircafe()
        elif opcion== "2":
            ver_historial()
        elif opcion == "3":
            print("\n Muchas gracias por haber tomado nuestros riquisimos cafes")
            break
        else:
            print("Opcion invalida, por favor indique una de las opciones sugeridas")

if __name__=="__main__":
    main()
