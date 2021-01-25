import random # Importing the Module.

while True: # Putting the Program within a loop.
    print(random.randint(1,6)) # Giving our program a range.
    Another_Throw = input("Want to roll the dice again? Enter(y/n): ") # Asking user for another input.
    
    if Another_Throw.lower() == "y": # Defining that if y is input then continue.
        continue

    if Another_Throw.lower() == "n": # Defining that if n is input then terminate.
        break

    else: # Putting an else condition so that the Program knows what to do in case of an invalid input.
        print("Invalid Input... The Program has Terminated itself...")
        break 