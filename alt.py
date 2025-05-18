from random import randint
pepo=0
try:
 dig1=int(input("Enter a number:\n"))
 dig2=int(input("Enter a second number:\n"))
 if dig2<dig1:
    while dig2<dig1:
        print("second number must be greater than first")
        dig2=int(input("Enter a second number:\n"))
 elif dig2>dig1:
    pepo=randint(dig1,dig2)
    for i in range (pepo):
        print ("▄")
except ValueError: print("ingreso erroneo")