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

#Declare inputs

#Score Table
cpu_score = 0
my_score  = 0

#Calculate
def calculate(cpu_hand, user_hand):
    if cpu_hand == user_hand:
        print(f"Both players selected {cpu_hand}")
        print(f"Tie! \nTry again")
    
    elif cpu_hand == "Rock" and user_hand == "Paper":
        print(f"CPU hand is {cpu_hand}")
        print("You Win!")
        my_score + 1
    elif user_hand == "Rock" and cpu_hand == "Paper":
        print(f"CPU hand is {cpu_hand}")
        print("CPU Wins!")
        cpu_score + 1

    elif user_hand == "Paper" and cpu_hand == "Rock":
        print(f"CPU hand is {cpu_hand}")
        print("CPU Wins!")

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



