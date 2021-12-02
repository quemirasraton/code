#Rock, paper, scissors
import random
from typing import NewType

options: list[str] = ["Rock", "Paper", "Scissors"]

#Banner
print("Welcome to the ultimate game!\nRock, Paper, Scissors!")
# User chose and option
user_hand: str = input("\nChoose your hand\n")
# CPU choses randomly an option
cpu_hand: str = random.choice(options)

#Constantes
user_action = user_hand
computer_action = cpu_hand
#Declare inputs

#Score Table
cpu_score = 0
my_score  = 0

#Calculate
def calculate(cpu_hand, user_hand):
    if cpu_hand == user_hand:
        print(f"Tie! \nTry again")
    elif cpu_hand == "Rock" and user_hand == "Paper":
        print(f"CPU hand is {cpu_hand}")
        print("You Win!")
        my_score + 1

    elif user_hand == "Rock" and cpu_hand == "Paper":
        print(f"CPU hand is {cpu_hand}")
        print("CPU Wins!")
        cpu_score + 1
    elif cpu_hand  == "Paper" and user_hand == "Scissors":
        print(f"CPU hand is {cpu_hand}")
        print("You Win!")
        my_score + 1
    elif user_hand == "Paper" and cpu_hand == "Scissors":
        print(f"CPU hand is {cpu_hand}")
        print("CPU Wins!")
        cpu_score + 1

    elif cpu_hand  == "Rock" and user_hand == "Scissors":
        print(f"CPU hand is {cpu_hand}")
        print("CPU Wins!")
        cpu_score + 1
    elif user_hand  == "Rock" and cpu_hand == "Scissors":
        print(f"CPU hand is {cpu_hand}")
        print("You Win!") 
        my_score + 1
    
calculate(cpu_hand, user_hand)

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")





