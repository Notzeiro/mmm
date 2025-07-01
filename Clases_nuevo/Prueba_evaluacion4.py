import os
compradores={1:{ "nombre":"link" , "tipo_de_entrada":"V" , "codigo_de_confirmacion":"unodosTRES4" } ,
 2:{ "nombre":"peppo" , "tipo_de_entrada":"G" , "codigo_de_confirmacion":"HOSTIAhola999" }

 }
def valida_nombre():
 while True:
    nombre=input("Nombre del comprador: ")
    if not nombre.isalpha():
        print("Ingrese solo letras")
        continue
    if len(nombre)<1:
        print("Largo invalido")
        continue
    return nombre
def valida_tipo_de_entrada():
 while True:
    tipo_de_entrada=input("Tipo de entrada (G, V): ")
    match tipo_de_entrada:
        case "G":
            print("Seleccionado tipo de entrada general")
            return tipo_de_entrada
        case "V":
            print("Seleccionado tipo de entrada VIP")
            return tipo_de_entrada
        case _:
            print("Opcion invalida")
            continue

def valida_codigo_de_confirmacion():
 while True:
    mayuscula=0
    numero=0
    codigo_de_confirmacion=input("Codigo de confirmacion: ")
    if len(codigo_de_confirmacion)<6:
        print("mínimo 6 caracteres")
        continue
    for char in codigo_de_confirmacion:
        if char.isupper():
            mayuscula+=1
        if char.isdigit():
            numero+=1
        
    if numero==0:
        print("Debe incluir un número")
        continue
    if mayuscula==0:
        print("Debe incluir una mayúscula")
        continue
    if numero>=1 and mayuscula>=1:
            print("Codigo registrado exitosamente")
            return codigo_de_confirmacion
def comprar_entrada(dictionary):

 os.system("cls")
 print("COMPRAR ENTRADA")

 nombre=valida_nombre()

 tipo_de_entrada=valida_tipo_de_entrada()

 codigo_de_confirmacion=valida_codigo_de_confirmacion()

 compra_nueva={ "nombre":nombre , "tipo_de_entrada":tipo_de_entrada , "codigo_de_confirmacion":codigo_de_confirmacion }
 
 last_id=list(dictionary.keys())
 dictionary[last_id[-1]+1]=compra_nueva
def consultar_comprador(dictionary):
 encontrado=False
 while True:
    if encontrado==True:break
    os.system("cls")
    nombre_a_buscar=input("Ingrese nombre a buscar: ")
    for key , value in dictionary.items():
        if nombre_a_buscar in value["nombre"]:
            print("Comprador encontrado")
            print(f"Nombre: {value["nombre"]}")
            print(f"Tipo de entrada: {value["tipo_de_entrada"]}")
            print(f"Codigo de confirmacion: {value["codigo_de_confirmacion"]}")
            input("")
            encontrado=True
            break
    else:
        encontrado=False
        print("El comprador no se encuentra")
        input("")
        break
def cancelar_compra(dictionary):
 encontrado=False
 while True:
    if encontrado==True:break
    nombre_a_cancelar=input("Ingrese nombre a cancelar: ")
    for key , value in dictionary.items():
        if nombre_a_cancelar in value["nombre"]:
            print("Compra cancelada")
            del(dictionary[key])
            encontrado=True
            break
        else:
            encontrado=False
            print("El comprador no se encuentra")
            input("")
            break
def menu():
 while True:
    print("""
    MENU PRINCIPAL
    1.-Comprar entrada
    2.-Consultar comprador
    3.-Cancelar compra
    4.-Salir
    """)
    op=input("Ingrese opcion: ")
    match op:
        case "1":
            comprar_entrada(compradores)
        case "2":
            consultar_comprador(compradores)
        case "3":
            cancelar_compra(compradores)
        case "4":
            print("Adios")
            break
        case "print": #DEV PURPOSES IGNORE....
            for key, value in compradores.items():
                print(key , ":" , value)
            input("")
        case _:
            print("Ingreso erroneo")
#iniciar el programa
menu()