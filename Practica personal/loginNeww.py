import os, time

database=[]
regSuccess=False


def ct():
    os.system("cls")


def menu():
    try:
        while True:
            ct()
            op=input("1.-Log in \n2.-Register \n3.-Exit\n")
            match op:
                case "1":
                    login()
                    

                case "2":
                    regSuccess=False
                    register()
                    
                 
                case "3":
                    
                    print("bye")
                    break

                case _:
                    print(f"""Please enter a valid option "{op}" isn't an option""")
                    input("Press anything to continue..")

    except Exception as a:
        print(f"ERROR, sorry something happened..  {a}")
        input("press anything to go back..\n")
    



def register():
    global database, regSuccess
    try:
        while True:
            ct()
            if regSuccess==True:
                break
            useraccepted=False
            user=input("Enter your user:\n")
            while True:
                ct()
                q=input(f"your username will be {user}, is that correct?\n1.-Yes\n2.-No\n")
                match q:
                    case "1":
                        useraccepted=True
                        break          
                    case "2":
                        break
                    case _:
                        print(f"""Please enter a valid option "{q}" isn't an option""")
                        input("Press anything to continue..")
            while useraccepted:
                acceptablePasswd=False
                specialCharacters= r''' !@#$%^&*()_+-={}[]\\|;:\'\"<>,.?/~` '''
                ct()
                print("Password creation\n\n-8 characters minimum\n-Have at least 1 special character\n")

                passwd=input("Enter your password: ")

                if len(passwd)<8:
                    print("-8 characters minimum!!")
                    input("press anything to continue..")
                    continue
                else:
                    for letter in passwd:
                        if letter in specialCharacters:
                            acceptablePasswd=True
                            break
                    if not acceptablePasswd:
                        print("-Have at least 1 special character!!")
                        input("press anything to continue..")
                        continue

                if acceptablePasswd==True:
                    while True:   
                        passwdRepeat=input("Repeat your password:\n")
                        if passwd==passwdRepeat:
                           userid=(f"user{len(database)+1}")
                           userid={
                                      "username":user,
                                      "password":passwd 

                                      }
                            
                           database.append(userid)
                           ct()
                           print("Register success, you may now log in the system")
                           time.sleep(1.5)
                           regSuccess=True
                           useraccepted=False
                           break
                        else:
                            print("Passwords don't match\n")
                            continue
                            



                    

                


    except Exception as a:
        print(f"ERROR, sorry something happened..  {a}")
        input("press anything to go back..\n")


def login():
    ct()
    userFound=False
    passwordMatch=False
    userAttempt=input("Enter your user:\n")
    passwordAttempt=input("Enter your password:\n")
    for user, username, password in database:
        if userAttempt==username:
            userFound=True
            if passwordAttempt==password:
                passwordMatch=True
                break
    if userFound and passwordMatch:
        print(f"Welcome {userAttempt}")
    

    


menu()