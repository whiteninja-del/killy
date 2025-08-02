import random
import sys

from random import shuffle

opts=['rock','paper','scissors']
print("\n".join(opts))

user_input=input("\nChoose One:\n")
comp_choice=random.choice(opts)
if user_input=="rock":
    random.shuffle(opts)

    if comp_choice=="rock":
        print("Computer chose:", comp_choice)
        print("\nYou Win.")
    elif comp_choice=="paper":
        print("Computer Chose:", comp_choice)   
        print("\nComputer Wins") 
    elif comp_choice=="scissors":
        print("Computer Chose:", comp_choice)   
        print("\nComputer Wins.") 
    else:
        sys.exit() 
elif user_input=="paper":
    random.shuffle(opts)

    if comp_choice=="paper":
        print("Computer Chose:", comp_choice)
        print("\nYou Win")
    elif comp_choice=="rock":
        print("Computer Chose:", comp_choice)  
        print("\nComputer Wins") 
    elif comp_choice=="scissors":
        print("Computer Chose:", comp_choice)    
        print("\nComputer Wins")
    else:
        sys.exit()  

elif user_input=="scissors":
    random.shuffle(opts) 

    if comp_choice=="scissors":
        print("Computer Chose:", comp_choice)  
        print("\nYou Win")  
    elif comp_choice=="rock":
        print("Computer Chose:", comp_choice)     
        print("\nComputer Wins.")  
    elif comp_choice=="paper":
        print("Computer Chose:", comp_choice)   
        print("\nComputer Wins") 
    else:
        sys.exit() 
else:
    print("Invalid Input.") 
    sys.exit()          
  