# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")
# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals

if (user_choice == "r"):
    if (computer_choice == "r"):
        print("rock tie!")
    elif (computer_choice == "p"):
        print("rock lose to paper!")
    elif (computer_choice == "s"):
        print("rock wins scissor!")    
elif (user_choice == "p"):
    if (computer_choice == "p"):
        print("paper tie!")
    elif (computer_choice == "s"):
        print("paper lose to scissor!")
    elif (computer_choice == "r"):
        print("paper wins rock!")       
elif (user_choice == "s"):
    if (computer_choice == "s"):
        print("scissors tie!")
    elif (computer_choice == "r"):
        print("scissors lose to rock!")
    elif (computer_choice == "p"):
        print("scissors wins paper!")   
else:
    print("what the fuck you typing?")