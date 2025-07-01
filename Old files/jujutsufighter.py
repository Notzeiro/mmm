import pyfiglet
from random import randint
import time
import os
from termcolor import colored
welcome=pyfiglet.figlet_format("Jujutsu Kaisen Fighter")



def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()



SatoruGojo={"Name":"Satoru Gojo"
,"HP":3000 , 
"CursedEnergy":4000 , 
"PS":470 , 
"Speed":500 , 
"color":"magenta" ,
 "attacks":["Red" , "Blue" , "HollowPurple"  , "Teleportation" , ] ,
 "abilities":["ReversedCursedTechnique" , "Teleportation"] ,
 "phrases":["You are weak" , "My students are watching so Im gonna show off a little" , "Nah I'd win"] ,
 "ultimate":{"Name":"Unlimited Void"}}


RyomenSukuna={"Name":"Ryomen Sukuna",
"HP":8000, 
"CursedEnergy":8000,
 "PS":500, 
 "Speed":500 , 
 "color":"red" ,
 "phrases":["You hold your head quite high" , "Not bad for a brat" , "You jujutsu sorcerers are a pain"],
 "attacks":["Slash" , "Dismantle" , "Cleave" , "DivineFlame" , ],
 "abilities":["ReversedCursedTechnique"],
 "ultimate":{"Name":"Malevolent Shrine"}}


FushiguroToji={"Name":"Fushiguro Toji"
,"HP":1200, 
"CursedEnergy":0, 
"PS":1000, 
"Speed":600 , 
"color":"light_grey" ,
"attacks":["JawKick" , "Left Punch" , "piercing strike" , "Brutal barrage"],
"abilities":["Inverted Nullification", "Hidden arsenal"]}


FushiguroMegumi={"Name":"Fushiguro Megumi",
"HP":1000, 
"CursedEnergy":1200, 
"PS":90, 
"Speed":100 
,"color":"black"}
# FM=[]
YujiItadori=[2000, 600, 260, 120]
YujiItadori={"Name":"Yuji Itadori", 
"HP":2000 , 
"CursedEnergy":600, 
"PS":260, 
"Speed":120 , 
"color":"light_red"}
# YI=[]

Characters=[SatoruGojo , RyomenSukuna , FushiguroToji , FushiguroMegumi , YujiItadori]

print(f"{welcome}By:NotZeiro\n------------------------------------------------------------\nPress anything to continue")
h=input("")



while True:
    print("MAIN MENU\n-----------------------\n1.-Player vs Player\n2.-Player vs COM \n3.-Characters\n4.-Exit")
    menu=int(input(""))
    if menu==1:
        print("")
        #main game
        print("Player 1 Choose your character:")
        for index , i  in enumerate(Characters):
                print (f"{index+1}.-{i["Name"]}")
        selection=int(input(""))
        Player1=Characters[selection-1]
        p1color=Player1["color"]

        msg1="Player 1 will play as "
        p1cn=colored(Player1["Name"] , p1color)

        print (msg1 + p1cn)


        
        print("-----------------------------------------------------")
        print("Player 2 Choose your character:")   
        for index , i  in enumerate(Characters):
                print (f"{index+1}.-{i["Name"]}")
        selection2=int(input(""))
        if selection2==selection:
            
            while selection2==selection:
                print(f"Cannot play as {Player1["Name"]}\nPlease select another character\n")
                print("Player 2 Choose your character:")   
                for index , i  in enumerate(Characters):
                 print (f"{index+1}.-{i["Name"]}")
                selection2=int(input(""))



        Player2=Characters[selection2-1]
        p2color=Player2["color"]


        msg11="Player 2 will play as "
        p2cn=colored(Player2["Name"] , p2color)


        print (msg11 + p2cn)
        



        p=input("Press anything to start")
        clear_terminal()

    

        vs=pyfiglet.figlet_format(f"{Player1["Name"]}  vs  {Player2["Name"]}")
        print(vs)
        time.sleep(4)
        turn=randint(1,2)
        if turn%2==0:
            print(f"{p1cn} will start")
        elif turn%2!=0:
            print(f"{p2cn} will start")

        
        while Player1["HP"]>0 or Player2["HP"]>0:
            if turn%2==0:
                #player1 turn
                print(f"{Player1["Name"]} \nHealth={Player1["HP"]} CursedEnergy={Player1["CursedEnergy"]}")
                print("----------------------------------------------------------------------------------")
                p1t=int(input(f"1.-Attack\n2.-Abilities\n"))
                if p1t==1:
                    for index , i  in enumerate(Player1["attacks"]):
                     print (f"{index+1}.-{i}")
                     
                    print(f"{len(Player1["attacks"]) + 2}.-{Player1["ultimate"]["Name"]}")    
                    
                    p1at=int(input(""))
                elif p1t==2:
                    for index , i  in enumerate(Player1["abilities"]):
                     print (f"{index+1}.-{i}")
                     p1ab=int(input(""))
                
            elif turn%2!=0:
                #player2 turn
                print(f"{Player2["Name"]} \nHealth={Player2["HP"]} CursedEnergy={Player2["CursedEnergy"]}")
                print("----------------------------------------------------------------------------------")
                p2t=int(input(f"1.-Attack\n2.-Abilities\n"))
                if p2t==1:
                    for index , i  in enumerate(Player2["attacks"]):
                     print (f"{index+1}.-{i}")
                     
                    print(f"{len(Player2["attacks"]) + 2}.-{Player2["ultimate"]["Name"]}")    
                    p2at=int(input(""))
                elif p2t==2:
                    for index , i  in enumerate(Player2["abilities"]):
                     print (f"{index+1}.-{i}")
                     p2ab=int(input(""))






    elif menu==2:
        print("Available soon!\nPress anything to go back")
        h=input("")
        continue
    elif menu==3:
        k=int(input("Character bible\n1.-See Characters\n2.-Back\n"))
        if k==1:
            print("Character list\n--------------------------")
            for index , i  in enumerate(Characters):
                print (f"{index+1}.-{i["Name"]}")
            Soo=int(input("Choose a character or press 0 to go back"))
            if soo==0:
                continue
            else:
                print("pepo")     
                #this should show the character abilities
        elif k==2: 
            continue                    
    elif menu==4:
        print("Bye!")    
        break