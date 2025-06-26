import os


users={}

def clear_terminal():
    os.system("cls")

def user_login():
    global users
    clear_terminal()
    while True:
        try:
            clear_terminal()
            op=input("------------------------------------\n        L O G   I N      \n------------------------------------\n\n1.-Log in \n2.-Back\n")
            match op:
                case "1":
                       attempts=0
                       clear_terminal()
                       userN=input("Enter your user:\n")
                       
                       for user, user_data in users.items():
                           if userN==user_data["username"]:
                            sel_user=user_data["username"]
                            passN=input(f"Enter the password for {sel_user}:\n")
                            if passN==user_data["password"]:
                                a=input("SUCCESFUL LOG IN")
                            else:
                                attempts+=1
                                
                            


                case "2":
                    break
                case "hola":

                    print(users)
                    print ("hola")
                    a=input("a")
                case _:
                    print("Invalid option :[")
                    a=input("Press anything to go back..")



        except Exception as o:
            print (f"Sorry unexpected error: {o}")
            a=input("Press anything to go back..")




def user_register():
    global users
    while True:
        try:
            clear_terminal()
            op=input("------------------------------------\n     U S E R   R E G I S T E R      \n------------------------------------\n\n1.-Register \n2.-Back\n")
            match op:
                case "1":
                    clear_terminal()
                    created=False
                    while True:
                        
                        if created==True:
                            break
                        name=input("Enter your user:\n")
                        if len(name)<3:
                            print("Your user is to short (3 characters minimum)")
                            continue
                        else:

                            if name in users:
                                print("User not available")  
                                continue  
                            else:
                                clear_terminal()
                                op=input(f"Your user will be {name}, is that correct?\n1.-Yes\n2.-No\n")   
                                match op:
                                    case "1":
                                        while True:
                                            clear_terminal()
                                            passwd=input("Create a password:\n")
                                            passwd2=input("Repeat your password:\n")

                                            if passwd==passwd2:
                                                print("Saved correctly")
                                                users[f"user{(len(users)+1)}"]={"username":name , "password":passwd}
                                                a=input("Press anything to go back..")
                                                created=True
                                                break
                                            else:
                                                print("Passwords don't match")
                                                a=input("Press anything to go back..")
                                                continue
                                    case "2":                                       
                                        continue
                                    case _:
                                        print("Invalid option :[")
                                        a=input("Press anything to go back..")
                case "2":
                    break
                case _:
                    print("Invalid option :[")
                    a=input("Press anything to go back..")



        except Exception as o:
            print (f"Sorry unexpected error: {o}")
            a=input("Press anything to go back..")



def program():
    global users
    while True:
        try:
            clear_terminal()
            op=input("-------------------------\n     W E L C O M E      \n-------------------------\n\n1.-Log in \n2.-Register\n3.-Exit\n")
            match op:

                case "1":
                    user_login()
                case "2":
                    user_register()
                case "3":
                    clear_terminal()
                    print("Bye")
                    break
                case _:
                    print("Invalid option :[")
                    a=input("Press anything to go back..")
                
        except Exception as o:
            print (f"Sorry unexpected error: {o}")
            a=input("Press anything to go back..")



program()