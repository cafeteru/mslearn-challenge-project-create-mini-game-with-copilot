from enum import Enum

class Choice(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == Choice.ROCK and computer_choice == Choice.SCISSORS) or \
       (user_choice == Choice.SCISSORS and computer_choice == Choice.PAPER) or \
       (user_choice == Choice.PAPER and computer_choice == Choice.ROCK):
        return "User wins!"
    else:
        return "Computer wins!"

while True:
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    try:
        user_choice = Choice(choice)
        print(f"You chose {user_choice.name}.")
        break
    except ValueError:
        print("Invalid choice. Please enter rock, paper, or scissors.")

import random
computer_choice = random.choice(list(Choice))
print(f"Computer chose {computer_choice.name}.")

print(determine_winner(user_choice, computer_choice))