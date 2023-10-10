import random

def get_player_choice(player_name):
    while True:
        choice = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").lower()
        if choice in ('rock', 'paper', 'scissors'):
            return choice
        else:
            print("Invalid choice. Please choose from rock, paper, or scissors.")

def determine_winner(player1, player2, player3):
    if player1 == player2 == player3:
        return "It's a tie!"
    elif (player1 == player2) or (player1 == player3) or (player2 == player3):
        return "It's a three-way tie!"
    elif (
        (player1 == 'rock' and player2 == 'scissors' and player3 == 'scissors') or
        (player1 == 'paper' and player2 == 'rock' and player3 == 'rock') or
        (player1 == 'scissors' and player2 == 'paper' and player3 == 'paper')
    ):
        return "Player 1 wins!"
    elif (
        (player2 == 'rock' and player1 == 'scissors' and player3 == 'scissors') or
        (player2 == 'paper' and player1 == 'rock' and player3 == 'rock') or
        (player2 == 'scissors' and player1 == 'paper' and player3 == 'paper')
    ):
        return "Player 2 wins!"
    else:
        return "Player 3 wins!"

def main():
    print("Welcome to the three-player Rock-Paper-Scissors game!")
    player1 = get_player_choice("Player 1")
    player2 = get_player_choice("Player 2")
    player3 = get_player_choice("Player 3")

    print(f"Player 1 chose {player1}")
    print(f"Player 2 chose {player2}")
    print(f"Player 3 chose {player3}")

    result = determine_winner(player1, player2, player3)
    print(result)

if __name__ == "__main__":
    main()
