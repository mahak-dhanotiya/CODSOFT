# ROCK-PAPER-SCISSORS GAME 

import random

print("--------------- \"ROCK-PAPER-SCISSORS GAME\" ---------------")

user_score = 0
computer_score = 0 

choice = "Yes"

while choice.lower() == "yes":
    
    # User Input
    print("\nEnter Your Choice (Rock/Paper/Scissor): ")
    user_input = input()
    
    # Checking user input 
    if user_input.lower() == "exit":
        break
    
    if user_input.lower() not in["rock", "paper", "scissor"]:
        print("Invaild input! Enter valid input.")
        continue

    # Computer Selection 
    computer_choice = random.choice(["Rock", "Paper", "Scissor"])

    # Game Logic
    def game_logic(user_input, computer_choice):
        global user_score, computer_score  # Accessing global variables
        
        user = user_input.lower()
        computer = computer_choice.lower()
        
        if user == computer:
            return "It's a tie!!"
        elif (user == "rock" and computer == "scissor") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissor" and computer == "paper"):
            user_score += 1
            return "User wins!!"
            
        elif user in ["rock", "paper", "scissor"]:
            computer_score += 1
            return "User loses!!"
            
        else:
            return "Invalid choice!"


    # Show choices and result
    print("\n        Choices are :")
    print("User's choice is :", user_input)
    print("Computer's choice is :", computer_choice)
    
    print("\nResult:", game_logic(user_input, computer_choice))


    # Ask if user wants to play again
    choice = input("\nWant to play another round? (Yes/No): ")
    
    if (choice.lower() == "yes"):
        continue
    else:
        if (user_score > computer_score):
            print("\nUser wins the game having final score = ",user_score)
        elif(computer_score > user_score):
            print("\nComputer wins the game having final score = ",computer_score)
        else:
            print("\nIt's a TIE between you both!!",user_score,computer_score)
            
        print("\nThanks for playing! Bye!!")
