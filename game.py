## create a simple rock, paper and scissor game
## provide a welcome message
## ask the user to choose between rock, paper and scissor
## generate a random choice for the computer
## compare the user's choice with the computer's choice
## print the results
## ask the user if they want to play again
## if yes, repeat the game
## if no, print a goodbye message

import random

def play_round(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissor":
            return "You win!"
        else:
            return "You lose!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        else:
            return "You lose!"
    elif user_choice == "scissor":
        if computer_choice == "paper":
            return "You win!"
        else:
            return "You lose!"
    else:
        return "Invalid choice!"

def game():
    print("Welcome to the Rock, Paper, Scissor Game!")
    print("Please choose between rock, paper, and scissor.")
    user_choice = input("Your choice: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissor"])
    print("Computer's choice:", computer_choice)
    result = play_round(user_choice, computer_choice)
    print(result)
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    game()