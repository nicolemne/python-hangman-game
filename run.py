import random


def remaining_lives(lives):
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


def get_word():
    hidden_word = random.choice(open("cities.txt", "r").read().split('\n'))
    return hidden_word.upper()


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


def play_game(hidden_word):
    secret_word = "_" + " " * len(hidden_word)
    guessed = False
    guessed_letters = []
    lives = 9
    print("Good luck!")
    print(remaining_lives(lives))
    print(secret_word)
    print("\n")

    while not guessed and lives > 0:
        guess = input("Please guess a letter: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters: 
                print(f"{guess} has already been guessed")
            elif guess not in hidden_word:
                print(f"Not quite... {guess} is incorrect.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print(f"Nice! {guess} is in the word!")
                guessed_letters.append(guess)
        else:
            print("Not a valid guess.")
        print(remaining_lives(lives))
        print(secret_word)
        print("\n")


def start_options():
    """
    Function to display user choice to either 
    start game or view instructions
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
            instructions()

        else:
            print(f" You selected {choice}. "
                  "Please select S or H to continue ♥")


def instructions():
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


def main():
    intro_title()
    start_options()


main()
