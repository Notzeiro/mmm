import random, time
while True:
    try:
        perros=int(input("Ingrese la cantidad de perros: "))
        while perros<1:
            print("Debe ingresr 1 o mas perros")
            perros=int(input("Ingrese la cantidad de perros: "))
        cuota=4
        cumplen=0
        print("Los perros salieron de caza!!!")
        for p in range(perros):
            conejos=random.randint(0,8)
            time.sleep(1)
            if conejos>=cuota:
                print(f"El perro {p+1} trajo {conejos} conejos, cumplio la cuota")
                cumplen+=1
            else:
                print(f"El perro {p+1} trajo {conejos} conejos, se queda sin filete")
        print(f" El total de perros que cumplio la cuota fue {cumplen} ")
        print(f" El total de perros que no cumplio la cuota fue {perros-cumplen} ")
        break
    except Exception:
        print("Solo debes poner numeros enteros")
