import os

listaProductos=[1,2,3,4,5]



def lt():
    os.system("cls")

def product_delete():
    try:
        while True:
            lt()
            for index,element in enumerate(listaProductos):
                print(f"{index+1}.-{element}")
            destroy=int(input("Que producto desea eliminar?(numero)\n"))
            pepe=destroy-1
            if destroy>len(listaProductos):
                lt()
                print(f"Valor erroneo, no existe el producto numero {destroy}\n")
                input("Presiona cualquier tecla para continuar") 
                continue
            elif destroy<0:
                lt()
                print(f"Valor erroneo, no existe el producto numero {destroy}\n")
                input("Presiona cualquier tecla para continuar")
                continue
            else:
                productoEliminado=listaProductos[pepe]
                listaProductos.pop(pepe)
                print(f"producto {productoEliminado}, correctamente eliminado")
                input("Presiona cualquier tecla para continuar")
                return

    except ValueError:
        lt()
        print("Ingrese solo numeros")
        input("Presiona cualquier tecla para continuar")



def menu():
    global listaProductos
    try:
        while True:
            lt()
            op=input("1.-Agregar producto\n2.-Eliminar producto\n3.-Mostrar todos los productos ordenados\n4.-Salir\n")
            match op:

                case "1":
                    lt()
                    product=input("Ingresa el nombre del producto:\n")
                    listaProductos.append(product)
                    print(f"El producto {product} fue agregado correctamente")
                    
                case "2":
                    product_delete()
                    
                
                case "3":
                    lt()
                    listaProductos.sort
                    for index,element in enumerate(listaProductos):
                        print(f"{index}.-{element}")

                    aa=("")
                    input("Presiona cualquier tecla para continuar")

                    
                    
            

                case "4":
                    break
                    
                case _:
                    print("Opcion invalida")
                    aa=input("Presiona cualquier tecla para continuar")






    except Exception as a:
        lt()
        print(f"Hubo un error:[\n {a}")
        aa=input("Presiona cualquier tecla para continuar")


menu()