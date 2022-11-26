import random
import os


def hangman_remaining_lives(lives):
    hangman_lives = [
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        \n    ✝ ✝ ✝ ✝ ✝ ✝ ✝ ✝ ✝
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        \n    ♥ ✝ ✝ ✝ ✝ ✝ ✝ ✝
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        \n    ♥ ♥ ✝ ✝ ✝ ✝ ✝ ✝ ✝
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        \n    ♥ ♥ ♥ ✝ ✝ ✝ ✝ ✝ ✝
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        \n    ♥ ♥ ♥ ♥ ✝ ✝ ✝ ✝ ✝
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        \n    ♥ ♥ ♥ ♥ ♥ ✝ ✝ ✝ ✝
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        \n    ♥ ♥ ♥ ♥ ♥ ♥ ✝ ✝ ✝
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        \n    ♥ ♥ ♥ ♥ ♥ ♥ ♥ ✝ ✝
        """,
        """
        |/
        |
        |
        |
        |
        |
        ========
        \n    ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ✝
        """,

        """
        |
        |
        |
        |
        |
        ========
        \n    ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥
        """,
        """
        """
        ]
    
    return hangman_lives[lives]


hangman_intro_image = [
        """
        ___________
        |/        |
        ||        O
        ||       /|\\    Press » S  to start new game
        ||       / \\    Press » H  for instructions
        ||
        \n
        """,
        """
        """
]


def intro_title():
    """
    Function to display "Let's play Hangman" text when running the program
    """
    print("""
    █░░ █▀▀ ▀█▀ ▀ █▀   █▀█ █░░ ▄▀█ █▄█ 
    █▄▄ ██▄ ░█░ ░ ▄█   █▀▀ █▄▄ █▀█ ░█░ ▄ ▄ ▄
    """)
    print("""
    ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
    ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
    ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
    ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
    ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
    """)


def get_word():
    """
    Gets random word form cities.txt
    """
    word = random.choice(open("cities.txt", "r").read().split('\n'))
    return word.upper()


def start_options():
    """
    Function to display user choice to either
    start game or view instructions
    (User choice is displayed in the hangman_intro_image)
    """
    print(hangman_intro_image[0])
    
    options = False
    while not options:
        choice = input("\n ").upper()
        if choice == "S":
            options = True
            print("  Starting new game...")

        elif choice == "H":
            options = True
            hangman_instructions()

        else:
            print(f" You selected {choice}. "
                  "Please select S or H to continue ♥")


def hangman_instructions():
    """
    Function to display help instructions for game rules.
    Starts the game when user enters S
    """
    print("\n")
    print("A name of a city will be hidden behind blank spaces.\n"
          "You must find the correct city by guessing each letter.\n"
          "Correct guesses will reveal a letter in the name.\nWrong guesses "
          "will reduce a life. You have 7 lives.\n\nHope you have fun!")
    print("\nPlease select S to play ♥")

    options = False
    while not options:
        choice = input("\n ").upper()
        if choice == "S":
            options = True
            print("Starting new game...")

        else:
            print(f" You selected {choice}. "
                  "Please select S play ♥")


def play_game(hangman_word):
    secret_word = "_" + " " * len(word)
    game_over = False
    guesses = []
    lives = 9
    print("Good luck!")
    print(f"Remaining Lives: {lives}\n")
    print("Your city to guess: " + " ".join(secret_word) + "\n")
    print("\n")

    while not game_over and lives > 0:
        input_guess = input("Please guess a letter: \n").upper()
        try:
            if len(input_guess) > 1: 
                raise ValueError(
                    f"Oops! You can only guess one letter at the time. "
                    f"You guessed: {len(input_guess)}."
                )
            elif not input_guess.isalpha():
                raise ValueError(
                    f"Oops! Only letters allowed."
                    f"You guessed: {len(input_guess)}."
                )
            elif len(input_guess) == 1 and input_guess.isalpha():
                if input_guess in guesses: 
                    raise ValueError(
                        f"You have already guessed {input_guess}."
                        )
                elif input_guess not in word:
                    print(f"Sorry, wrong guess... {input_guess}"
                          "is not in the word")
                    print("You lost a life. Better luck next time!")
                    guesses.append(input_guess)
                    lives -= 1
                else:
                    print(f"You found a letter! {input_guess} is correct. GG!")
                    guesses.append(input_guess)
                    guessed_word_list = list(secret_word)
                    indices = [i for i, letter in enumerate(input_guess)
                               if letter == input_guess]
                    for index in indices:
                        guessed_word_list[index] = input_guess
                        secret_word = "".join(guessed_word_list)
                    if "_" not in secret_word:
                        game_over = True
        
        except ValueError as e:
            print(f"{e}.\n Please try again.\n")
            continue

        print(hangman_remaining_lives(lives))

        if lives > 0:
            print(f"Remaining Lives: {lives}\n")
            print(f"Your city to guess: " + " ".join(secret_word) + "\n")
            print(" Your guesses: " + ", ".join(sorted(input_guess)) + "\n")

    if game_over:
        print(f"Congrats, you found the secret word: {secret_word}!")
    
    else:
        print(f"Oh shoot! You're out of lives.")
        print("Game over.\n\n")
        print(f"The correct word was: {secret_word}")


def main():
    intro_title()
    start_options()
    hangman_word = get_word()


main()
