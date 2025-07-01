from random import randint
import math
pepo=[]
def numMasCercano():
 numero1=abs(misterynumber-pepo[0])
 numero2=abs(misterynumber-pepo[1])
 if numero1<numero2:
    return pepo[0]
 elif numero2<numero1:
    return pepo[1]

def numMenosCercano():
 numero1=abs(misterynumber-pepo[0])
 numero2=abs(misterynumber-pepo[1])
 if numero1<numero2:
    return pepo[1]
 elif numero2<numero1:
    return pepo[0]
num1=int(input("Ingrese un numero:\n"))
num2=int(input("Ingrese un numero mas grande que el anterior:\n"))
while num2<num1:
 print(f"El numero debe ser mayor que {num1}")
 num2=int(input("Ingrese un numero:\n"))
misterynumber=randint(num1,num2)
momo=False
a=False
b=False
guess=int(input("Adivine el numero:\n"))
pepo.append(guess)
if guess==misterynumber:
 print("Felicidades adivinaste")
 momo=True
 a=True
if guess<misterynumber and momo==False:
 print("el numero es mayor")
elif guess>misterynumber and momo==False:
 print("el numero es menor")
if a==False:
 guess=int(input("Intente denuevo:\n"))
 pepo.append(guess)
if guess==misterynumber:
 print("Felicidades adivinaste")
 momo=True
 b=True
if guess<misterynumber and momo==False:
 print("el numero es mayor")
 print(f"te dare una pista, el numero que buscas esta mas cerca de {numMasCercano()} que de {numMenosCercano()}")
elif guess>misterynumber and momo==False:
 print("el numero es menor")
 print(f"te dare una pista, el numero que buscas esta mas cerca de {numMasCercano()} que de {numMenosCercano()}")
if b==False:
 guess=int(input("Intente una ultima vez:\n"))
if guess==misterynumber and b==False:
 print("Felicidades adivinaste")
else:
 print(f"perdiste, el numero era {misterynumber}")