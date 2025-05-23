import os

carrito=[]
names=[]
compra=False
def limpiar_terminal():
    os.system("cls")

def roll_selection():
    global carrito
    global compra
    try:
        while compra==False:
            limpiar_terminal()
            print("1. Pikachu Roll $ 4500")
            print("2. Otaku Roll $ 5000")
            print("3. Pulpovenenoso Roll $ 5200")
            print("4. Anguila electrica Roll $ 4800")
            print("5. Terminar compra")
            op=(input("Seleccione una opción: "))
            match op:
                case "1":
                    roll=4500
                    name="Pikachu Roll"
                    carrito.append(roll)
                    names.append(name)
                    ola=input("Agregado correctamente :)\npresione cualquier tecla para continuar..\n")
                case "2":
                    roll=5000
                    name="Otaku Roll"
                    carrito.append(roll)
                    names.append(name)
                    ola=input("Agregado correctamente :)\npresione cualquier tecla para continuar..\n")
                case "3":
                    roll=5200
                    name="Puppovenenoso Roll"
                    carrito.append(roll)
                    names.append(name)
                    ola=input("Agregado correctamente :)\npresione cualquier tecla para continuar..\n")
                case "4":
                    roll=4800
                    name="Anguila electrica Roll"
                    carrito.append(roll)
                    names.append(name)
                    ola=input("Agregado correctamente :)\npresione cualquier tecla para continuar..\n")
                case "5":
                    compra=True
                    carritoo()
                case _:
                    limpiar_terminal()
                    print("Seleccione una opcion valida")
                    a=input("Presione cualquier tecla para volver...\n")
    except Exception as asd:
        print(f"Lo sentimos, ocurrio un error inesperado:\n{asd}")

        
def carritoo():
    limpiar_terminal()
    X=input("Si posee un codigo de descuento ingreselo aqui, de lo contrario deje este espacio en blanco:\n")
    if X=="soyotaku":
        totald=sum(carrito)*0.9
        descuento=True
    else:
        descuento=False
    descuentopepo=sum(carrito)*0.1
    total=sum(carrito)
    limpiar_terminal()
    print("-------------------------")
    print("      B O L E T A     ")
    print("-------------------------")
    for index, elem in enumerate(names):
        print(f"{index+1}.-{elem}.........{carrito[index]} ")

    if descuento==True:
        print("descuento del 10% aplicado")
        print(f"Total del descuento:{descuentopepo}")
        print(f"Total de su compra: {totald}")
    else:
        print(f"Total de su compra: {total}")
  

roll_selection()
