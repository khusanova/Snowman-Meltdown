"""
Play the game "Melting snowman". The game can be played multiple times until
the user decides to quit.
"""

from game_logic import play_game


if __name__ == "__main__":
    print("Welcome to Snowman Meltdown!")
    while True:
        play_game()
        if input("Do you want to play again? [y/n]") != "y":
            break
