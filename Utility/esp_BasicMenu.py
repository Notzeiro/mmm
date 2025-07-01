import time, os

while True:
    os.system("cls")
    print("""
    1.- Opcion 1
    2.- Opcion 2
    3.- Opcion 3
    4.- Opcion 4
    5.- Salir
    """)
    
    op=input("Elija una opcion: ")
    
    match op:
        case "1":
            print("Opcion 1 seleccionada")
            input("Presione cualquier tecla para continuar...  ")
        case "2":
            print("Opcion 2 seleccionada")
            input("Presione cualquier tecla para continuar...  ")
        case "3":
            print("Opcion 3 seleccionada")
            input("Presione cualquier tecla para continuar...  ")
        case "4":
            print("Opcion 4 seleccionada")
            input("Presione cualquier tecla para continuar...  ")
        case "5":
            print("Adios")
            break
        case _:
            print(f"""Por favor ingrese una opcion valida "{op}" no es una opcion""")
            input("Presione cualquier tecla para continuar..  ")