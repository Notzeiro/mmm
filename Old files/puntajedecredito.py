sw=True
credito=0
try:
 while sw==True:
    nacionalidad=int(input("Cual es su nacionalidad?\n1.-Chilena\n2.-Extranjera\n"))
    nivel_educacional=int(input("Cual es su nivel de educacion?\n1.-Educacion basica\n2.-Educacion media\n2.-Educacion superior\n"))
    ingreso=int(input("Cual es su ingreso mensual?\n"))
    
    if ingreso>=500000 and ingreso<=1000000:
        credito=300000
    elif ingreso>=1000000 and ingreso<=1500000:
        credito=650000
    elif ingreso>1500000:
        credito=1000000
    if nivel_educacional==2:
        credito*=(130/100)
    elif nivel_educacional==3:
        credito*=(150/100)
    if nacionalidad==1:
        credito+=300000
    int(credito)
    pepo=int(input(f"Su credito es de {credito}\n desea calcular denuevo?\n1.-si\n2.-no\n"))
    if pepo==2:
        sw=False
except ValueError:print("Ingreso erroneo")

print("Adios")
