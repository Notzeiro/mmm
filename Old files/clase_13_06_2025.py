import os, time

notas=[5.0 , 4.6 , 7.0 , 6.5]

def notanueva():
    global notas
    notaValida=False
    try:
        os.system("cls")
        print("Ingrese numero con su respectivo punto EJ:(5.6)")
        pepe=float(input("Ingrese la nota: "))
        if pepe>=1.0 and pepe<7.0:
            notaValida=True
            
        else:
            print("ingrese una nota valida..")
            time.sleep(1.2)

        if notaValida:
            
            notas.append(pepe)
            print("Nota agregada correctamente..")
            input("Presione cualquier cosa para volver..")
    except ValueError:
        print("Error, ingrese solo numeros enteros")
        time.sleep(1.5)
        

def eliminar_nota():
    global notas
    try:
        print("(solo se permiten numeros enteros)")
        print(notas)
        pepe=float(input("Ingrese la nota a eliminar: "))
        
        notas.remove(pepe)
        print("Nota eliminada correctamente..")
        time.sleep(1.8)
    except ValueError:
        print("Error, ingrese solo numeros enteros")
        time.sleep(2)
    
def mostrar_notas():
    global notas
    os.system("cls")
    for index , nota in enumerate(notas):
        print(f"{index+1}.-{nota}")
    input("Presione cualquier cosa para volver..")

def promedio():
    global notas
    os.system("cls")
    suma=max(notas)+min(notas)
    promedioPEPO=suma/2
    print(f"El promedio de la nota mayor y la menor es de: {promedioPEPO} \nLas notas fueron {max(notas)} y {min(notas)}")
    input("presione cualquier tecla para volver...")

while True:
    os.system("cls")
    print(""" 
             1.-Ingresar nota
             2.-Borrar nota
             3.-Mostrar notas
             4.-Sacar promedio, nota mayor y nota menor
             5.-Limpiar todas las notas
             6.-Salir
             """)
    op=input("Seleccione una opcion: ")
    match op:
        case "1":
            notanueva()
        case "2":
            eliminar_nota()
        case "3":
            mostrar_notas()
        case "4":
            promedio()
        case "5":
            os.system("cls")
            while True:
                pepardo=input("Seguro que deseas borrar todas las notas? no se podran recuperar luego..\n1.-Si, borrar\n2.-No, volver\n")
                match pepardo:
                    case "1":
                        notas.clear()
                        print("Notas eliminadas correctamente")
                        time.sleep(2)
                        break
                    case "2":
                        break
                    case _:
                        print("opcion no valida " , (pepardo) , " no es una opcion")
                        time.sleep(2)
        case "6":
            print("adios")
            break
        case _:
            print("opcion no valida " , (op) , " no es una opcion")
            time.sleep(1.5)
    


