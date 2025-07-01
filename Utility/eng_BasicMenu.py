import time, os

while True:
    os.system("cls")
    print("""
    1.- Option 1
    2.- Option 2
    3.- Option 3
    4.- Option 4
    5.- Exit
    """)
    
    op=input("Choose an option: ")
    
    match op:
        case "1":
            print("Option 1 selected")
            input("Press any key to continue...  ")
        case "2":
            print("Option 2 selected")
            input("Press any key to continue...  ")
        case "3":
            print("Option 3 selected")
            input("Press any key to continue...  ")
        case "4":
            print("Option 4 selected")
            input("Press any key to continue...  ")
        case "5":
            print("Goodbye")
            break
        case _:
            print(f"""Please enter a valid option "{op}" is not an option""")
            input("Press anything to continue..  ")