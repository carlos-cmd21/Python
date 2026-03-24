#open(nombre,modo)
#Read r: solo lectura
#Write w: escritura, si el archivo no existe lo crea, si existe lo sobreescribe
# X create: crea el archivo, si existe lanza un error
#append: escritura, si el archivo no existe lo crea, si existe agrega al final del archivo

# try:
#     f=open("archivo.txt","r")
#     print(f.readline())
#     f.close()
# except FileNotFoundError:
#     print("El archivo no existe")

try:
    with open("archivo.txt","r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt","x")
    print("No se ha encontrado el archivo")


try:
    with open("archivo.txt","a") as f:
        f.write("\n")
        f.write("Hola mundo escrito desde el with")
    with open("archivo.txt","r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")