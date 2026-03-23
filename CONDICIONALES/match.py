dia =8

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("El numero no corresponde a un dia de la semana")


dia_nombre="carlos"
match dia_nombre:
    case "Lunes":
        print(f"El dia es : {dia_nombre}")
    case "Martes":
        print(f"El dia es : {dia_nombre}")
    case "Miercoles":
        print(f"El dia es : {dia_nombre}")
    case "Jueves":
        print(f"El dia es : {dia_nombre}")
    case "Viernes":
        print(f"El dia es : {dia_nombre}")
    case "Sabado":
        print(f"El dia es : {dia_nombre}")
    case "Domingo":
        print(f"El dia es : {dia_nombre}")
    case _:
        print("El nombre no corresponde a un dia de la semana")




