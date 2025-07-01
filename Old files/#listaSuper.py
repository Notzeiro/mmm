#listaSuper
sw = 1
listasuper = []
valorsuper = []

print("1.-Ingresar articulos \n0.-Salir")
op=int(input("Seleccione opción\n"))
if(op == 1):
    try:

        while sw==1:
         print("")
         producto=input("Ingrese el nombre del producto a agregar\n0.-Salir\n")
         if producto==0:
            break
         cantidad=int(input(f"¿Cuantas unidades de {producto} desea llevar?\n"))
         for i in range (cantidad):
          listasuper.append(producto)
         precio=int(input(f"Ingrese el precio de {producto}:\n"))
         for e in range (cantidad):
          valorsuper.append(precio)
         sw=int(input("¿Desea agregar otro producto?\n1.-si\n2.-no\n"))
            
    except:  #estas lineas son para errores de entrada por parte de los usuarios
            print("Ingreso Erróneo")
            
else:
    print("Adiós")


print("------------DETALLE BOLETA------------\nProductos         Precios")
for p in range (len(listasuper)):
    print ((listasuper [p]), ("          ") , (valorsuper [p]) )
    
print("---------------------------------------------------\nTotal:" , (sum(valorsuper)))
print("Total articulos: " , (len(listasuper)))

