import os, time

libro={}


def agregar_alumno():
    global libro
    os.system("cls")
    
    while True:
        os.system("cls")
        nombre=input("Ingrese el nombre del alumno: ").capitalize()
        q=input(f"El nombre {nombre} es correcto? \n1.-Si, continuar\n2.-No, modificar\n")
        if q=="1":
            a=False
            break
        elif q=="2":
            continue
    
    while True:
        os.system("cls")
        edad=input("Ingrese la edad del alumno: ")
        q=input(f"Es la edad {edad} correcta? \n1.-Si, continuar\n2.-No, modificar\n")
        if q=="1":
            b=False
            break
        elif q=="2":
            continue
        edad=int(edad)

    while True:
        os.system("cls")
        comuna=input("Ingrese la comuna de residencia del alumno: ")
        q=input(f"La comuna {comuna} es correcta? \n1.-Si, continuar\n2.-No, modificar\n")
        if q=="1":
            c=False
            break
        elif q=="2":
            continue
    
    while True:
        os.system("cls")
        ramos=input("Ingrese la cantidad de ramos del alumno: ")
        q=input(f"La cantidad de ramos {ramos} es correcta? \n1.-Si, continuar\n2.-No, modificar\n")
        if q=="1":
            d=False
            break
        elif q=="2":
            continue
    nombre_ramos=[]
    ramos=int(ramos)
    for ramo in range(ramos):
        while True:
            nombre_ramo=input(f"Ingrese el nombre del ramo n°{ramo+1}: ")
            q=input(f"El nombre {nombre_ramo} es correcto? \n1.-Si, continuar\n2.-No, modificar\n")
            if q=="1":
                break
            elif q=="2":
                continue
        nombre_ramos.append(nombre_ramo)
    id_alumno=(f"alumno{len(libro)+1}")
    libro[id_alumno]={"nombre":nombre,
                      "edad": edad,
                      "comuna": comuna,
                      "ramos": nombre_ramos}
    
def modificar_notas():
    global libro
    os.system("cls")

while True:
    os.system("cls")

    print(""" 
            1.-Ver libro de alumnos
            2.-Modificar libro de alumnos
            3.-Salir
            """)
    op=input("Ingrese una opcion: ")

    match op:
        case "1":
            print(libro)
            input("Presione cualquier tecla para continuar...  ")

        case "2":
            while True:
                os.system("cls")
                print("""
                    1.-Agregar alumno
                    2.-Modificar notas alumno
                    3.-Modificar ramos alumno
                    4.-Volver al menu principal
                        """)
                opp=input("Ingrese una opcion: ")
                match opp:
                    case "1":
                        agregar_alumno()


                    case "2":
                        print("en proceso")


                    case "3":
                        print("en proceso")

                    case "4":
                        break


                    case _:
                       
                        print("Ingrese una opcion valida, \"", opp, "\" no es una opcion valida...")
                        input("Presione cualquier tecla para continuar...   ")

        case "3":
            print("Adios")
            break

        case _:
            print("Ingrese una opcion valida, \"", op, "\" no es una opcion valida...")
            input("Presione cualquier tecla para continuar...   ")


