"""Game logic module.

Import play_game to run the game.
"""
import random

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
WIN_MESSAGE = "Congratulations, you saved the snowman!"
LOSE_MESSAGE = "Game over! The word was %s."


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Display game state:
        - Display ASCII art with the current state of the snowman;
        - Display the secret word with underscores for unguessed letters.
    """
    print(STAGES[mistakes])
    print("Word: ", end="")
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print("\n")


def get_letter():
    """
    Ask user to guess a letter until a valid input
    """
    while True:
        letter = input("Guess a letter: ").lower()
        if not letter.isalpha():
            print("This is not a letter.")
            continue
        if len(letter) != 1:
            print("Enter exactly one letter.")
            continue
        break

    print("You guessed:", letter)
    return letter


def play_game():
    """
    Play the "Melting snowman" game. Select a random word and let the user
    guess it by entering letters.
    """
    secret_word = get_random_word()
    all_letters = set(list(secret_word))
    mistakes = 0
    guessed_letters = []
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        # For now, simply prompt the user once:
        guess = get_letter()
        if guess in secret_word:
            guessed_letters.append(guess)
            if set(guessed_letters) == all_letters:
                print(WIN_MESSAGE)
                break
        else:
            mistakes += 1
            if mistakes > 3:
                print(LOSE_MESSAGE % secret_word)
                break
