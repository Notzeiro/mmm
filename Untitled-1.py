users=["user1", "user2", "user3", "notzeiro", "heterias"]
passwords=["1234","4321","1111","catita","hola123"]
bank=[500000 , 0 , 100000 , 350000 , 10000000]
access=True
trueaccess=False
tries=4


def showbalance():
  number=users.index(selected_user)
  print (bank[number])

#this below is the login system

while access==True:

    if tries<=0:
      access=False

    if access==True:
     selected_user=(input("Enter user: ")) #asks the user to enter a username on the list above
    elif access==False:
      print("We're sorry your access has been denied :[")
      break
    if selected_user in users: #if the username inpute above was correct it enters a while that asks for password
     while tries>0 and access==True:
      password_try=(input(f"Enter {selected_user}'s password: ")) #asks the user to enter password
      if password_try==passwords[users.index(selected_user)]:
          print(f"Welcome {selected_user} ")
          trueaccess=True
          trueuser=users.index(selected_user)
          access=False
      else:
        tries-=1
        print(f"Wrong password entered, you have {tries} attempts left")


    else: 
     print ("User misspelled or non existent, please try again")

if trueaccess==True: #From here starts the actual program
 number=users.index(selected_user)
 usersbalance=(bank[number])
 K5=30         #amount of bills in the atm
 K10=30
 K20=30
 p=True
while p==True:
 menu=int(input("1.-Show your balance\n2.-Withdraw\n3.-Deposit\n0.-Exit\n")) #ATM menu
 if menu==0:
  print("Bye ^^") #exit 
  break
 elif menu==1:
  print (f"{selected_user}s balance is:")
  showbalance()
  print("")
 elif menu==2:
  wanted_withdraw=int(input("How much would you like to withdraw?\n"))
  if wanted_withdraw>(bank[number]):
    print("\ninsufficient funds :[\nPlease select another option:\n")  
  elif wanted_withdraw<(bank[number]):
    

    # K20t=(wanted_withdraw//20000) #basic structure to sort the bills that will be given to the user
    # wanted_withdraw-=(K20t*20000)
    # K10t=(wanted_withdraw//10000)
    # wanted_withdraw-=(K10t*10000)
    # K5t=(wanted_withdraw//5000)
    # wanted_withdraw-=(K5t*5000)

    # K20-=K20t #this subtracts the given bills from the ATM
    # K10-=K10t
    # K5-=K5t
    usersbalance-=wanted_withdraw

    (bank[number])=usersbalance

    print(f"You withdrawed {wanted_withdraw} from your account\nyour new balance is {usersbalance}\n")
    #amount_to_substract=(bank[number])-wanted_withdraw #this is the amount that will be substracted from the user balance



    _20kbills=[]
    _10kbills=[]
    _5kbills=[]
    for h in range (30):
      _20kbills.append(20000)
      _10kbills.append(10000)
      _5kbills.append(5000)
 elif menu==3:
    wanted_deposit=int(input("How much will you deposit?\n"))   
    usersbalance+=wanted_deposit
    (bank[number])=usersbalance
    print(f"You deposited {wanted_deposit} to your account\nyour new balance is {usersbalance}\n")
