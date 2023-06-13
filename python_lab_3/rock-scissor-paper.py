" Disclaimer: This is a sample code for the Rock-Scissors-Paper game wriiten by ChatGPT."

import random

class RockScissorPaper:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0

    def get_player_choice(self):
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        while choice not in self.choices:
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice (rock/paper/scissors): ").lower()
        return choice

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'tie'
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
                (player_choice == 'paper' and computer_choice == 'rock') or \
                (player_choice == 'scissors' and computer_choice == 'paper'):
            return 'player'
        else:
            return 'computer'

    def play_round(self):
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()

        print(f"\nYou chose: {player_choice}")
        print(f"The computer chose: {computer_choice}")

        winner = self.determine_winner(player_choice, computer_choice)

        if winner == 'player':
            self.player_score += 1
            print("You win!")
        elif winner == 'computer':
            self.computer_score += 1
            print("Computer wins!")
        else:
            print("It's a tie!")

        print(f"Player score: {self.player_score}")
        print(f"Computer score: {self.computer_score}")

    def play_game(self):
        print("Welcome to Rock-Scissors-Paper Game!")
        print("Let's play!")

        play_again = 'y'
        while play_again.lower() == 'y':
            self.play_round()
            play_again = input("Do you want to play again? (y/n): ")

        print("Thanks for playing!")

# Create an instance of the game and play
game = RockScissorPaper()
game.play_game()
