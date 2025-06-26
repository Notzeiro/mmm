import os, time
def show_games(dictionary):
    for game, info in dictionary.items():
        print("---------------------------------")
        print(f"Nombre:{info["nombre"]}")
        print(f"Precio:{info["precio"]}")
        print(f"Codigo:{info["code"]}")
    input("Presione cualquier tecla para continuar...    ")

def add_games(dictionary):
    name=input("Ingrese nombre: ").capitalize()
    if not valida_nombre(name):
        while True:
            print("No puede ingresar un espacio al final... ")
            name=input("Ingrese nombre: ").capitalize()
            if valida_nombre(name): break

    while True:
        price=int(input("Ingrese precio: "))
        if valida_precio(price):
            break
        else:
            print("Precio debe ser entre 8.000 y 100.000")
    
    code=input("Ingrese codigo: ")

    game={"nombre" : name ,
        "precio": price ,
        "code" : code}
    
    hola=list(dictionary.keys())
    dictionary[hola[-1]+1]=game
    print("Agregado correctamente")
    time.sleep(1.2)

def delete_games(dictionary):
    for game, info in dictionary.items():
        print("---------------------------------")
        print(f"ID para borrar:{game}")
        print(f"Nombre:{info["nombre"]}")
        print(f"Precio:{info["precio"]}")
        print(f"Codigo:{info["code"]}")
    
    kill=int(input("Seleccione e juego a borrar: "))
    del dictionary[kill]

def valida_nombre(name):
    last_character=name[-1]
    if last_character.isspace():
        return False
    return True



def valida_precio(price):
    
    if price>=8000 and price<=100000:
        return True
    else:
        return False





juegos={
    1:{"nombre" : "Metroid Dread" ,
       "precio": 50000 ,
       "code" : "MTdr2023"} ,
    2:{"nombre" : "Luigi's Mansion" ,
       "precio": 58000 ,
       "code" : "LgMn2020"}
    
}

clave="momazo"
intentos=0
while True:
    claveIntento=input("Ingrese clave: ")
    if intentos<3:
        if claveIntento!=clave:
            print("gei")
            intentos+=1
        else:
            print("Bienvenido")
            time.sleep(1)
            while True:
                os.system("cls")
                print(""" 
                    1.- Mostrar juegos
                    2.- Eliminar Juegos
                    3.- Agregar juegos
                    4.- Salir
            """)
                op=input("Elija una opcion: ")
                match op:
                    case "1":
                        show_games(juegos)
                    case "2":
                        delete_games(juegos)
                    case "3":
                        add_games(juegos)
                    case "4":
                        print("Adios")
                        break

                    case _:
                        print(f"Por favor ingrese una opcion valida \"{op}\" no es una opcion valida..")
                        input("Presiona cualquier tecla para volver")

    else:
        print("Intentos agotados, intente en otro momento..")