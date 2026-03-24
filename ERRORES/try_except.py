try:
    numero=10 / 0
except ZeroDivisionError:
    print("No se puee dividir por cero")

x=1
try:
    print(x)
except NameError:
    print("La variable no esta definida")
finally:
    print("Esto se ejecuta siempre")
