'''
Create a Rock Paper Scissors game where the player inputs their choice and play against the computer thant randomly selects its move, with the game showing who won each round.
Add a score counter that tracks player and computer wins, and allow the game to continue until player types 'quit'.
'''

import random
def get_computer_choice():
    """Randomly select a choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def get_winner(player_choice, computer_choice):
    """Determine the winner of the game based on player and computer choices."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins!"
    else:
        return "Computer wins!"
def main():
    """Main function to run the Rock Paper Scissors game."""
    player_score = 0
    computer_score = 0

    print("Welcome to Rock Paper Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit the game.")

    while True:
        player_choice = input("Enter your choice: ").lower()
        if player_choice == "quit":
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(player_choice, computer_choice)
        print(winner)

        if winner == "Player wins!":
            player_score += 1
        elif winner == "Computer wins!":
            computer_score += 1

        print(f"Score - Player: {player_score}, Computer: {computer_score}")

    print("Thanks for playing!")
if __name__ == "__main__":
    main()
'''
# This code implements a simple Rock Paper Scissors game where the player can play against the computer.
# The player can input their choice, and the computer randomly selects its move.
# The game keeps track of the score and allows the player to quit at any time.
# The game is interactive and provides feedback on the outcome of each round.
# The game continues until the player types 'quit'.
# The code is structured with functions for better organization and readability.
# The main function runs the game loop and handles user input.
# The get_computer_choice function randomly selects a choice for the computer.
# The get_winner function determines the winner based on the player's and computer's choices.
# The game is designed to be user-friendly and provides clear instructions for the player.
# The game uses a while loop to keep running until the player decides to quit.
# The player can input their choice in lowercase to ensure consistency.
# The game provides feedback on invalid choices and prompts the player to try again.
# The game keeps track of the score for both the player and the computer.
# The game displays the current score after each round.
# The game is designed to be simple and easy to understand, making it suitable for players of all ages.
# The game can be easily extended or modified to include additional features or rules.
# The code is written in Python and can be run in any Python environment.
# The game can be played in a terminal or command prompt.
# The game can be easily adapted for different platforms or interfaces.
# The game can be enhanced with additional features such as graphics or sound effects.
# The game can be used as a fun way to practice programming skills and learn about game development.
# The game can be shared with friends or family for entertainment.
# The game can be used as a learning tool for beginners to understand basic programming concepts.
# The game can be used as a fun way to practice decision-making and strategy.
# The game can be used to explore concepts such as randomness and probability.
'''