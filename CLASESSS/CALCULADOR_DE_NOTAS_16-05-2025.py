import pyfiglet
welcome=pyfiglet.figlet_format("Calculadora de notas")
alumnos=[]
def busqueda_alumno():
    busqueda=(input("Ingrese nombre del alumno:\n"))
    for alumno in alumnos:
        if busqueda==alumno:
            print(f"Nombre={"nombre"}")
            print(f"Nombre={"notas"})



def ingreso_alumnos():
    global alumnos
    try:
        a=int(input("Ingrese la cantidad de alumnos:\n"))
        if a>0:
            for i in range (a):
                nombre=input(f"ingrese el nombre del alumno {i+1}:\n")
                notasb=int(input(f"Ingrese la cantidad de notas del alumno {nombre}:\n"))
                notaslista=[]
                for d in range(notasb):
                    
                    notas=(int(input(f"Ingrese la nota n°{d+1} de {nombre}:\n")))
                    notaslista.append(notas)
                alumno={"nombre":nombre ,
                            "Notas" : notaslista ,
                            "promedio": sum( notaslista ) / len( notaslista )}
                alumnos.append(alumno)
                
            
        else:
            print("por favor ingrese una cantidad valida")
    except:
        print("Error, ingreso erroneo")

def menu():
    while True:
        try:
            op=(int(input("1.-Buscar alumno\n2.-Ingresar mas alumnos\n3.-Salir\n")))
            if op!=1 or op!=2 or op!=3:
                print("Por favor ingrese una opcion valida")
                continue
            match op:
                case 1:
                    busqueda_alumno()
                    
                case 2:
                    ingreso_alumnos()
                case 3:
                    print("Adios")
                    break

        except:
            print("Error, ingreso erroneo")



print(welcome)
ingreso_alumnos()



