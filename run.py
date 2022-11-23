import random

hangman_images = [
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


def random_city():
    hidden_word = random.choice(cities)
    print(hidden_word.upper())


# Capital cities word bank
cities = ('dublin reykjavik cardiff edinburgh belfast london oslo stockholm '
          'helsinki berlin copenhagen amsterdam brussels paris '
          'luxembourg lisbon madrid rome bern vienna warsaw '
          'prague bratislava vilnius riga tallinn bucharest budapest '
          'zagreb sarajevo ljubljana belgrade skopje sofia pristina '
          'minsk kiev tbilisi athens ankara vaduz podgorica valetta tirana '
          'nicosia chisinau moscow monaco tokyo seoul bejing kathmandu cairo '
          'canberra hanoi lima ottawa jerusalem santiago brasilia kingston '
          'havana wellington pyongyang taipei bangkok manila jakarta '
          'mogadishu ulaanbataar ').split()


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


def start_game():
    correct_guess = ''
    wrong_guess = ''

    print("\n")
    print("\n")

    # testing
    return random_city()


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
    # print(hangman_intro_image[0])
    # print("   Welcome to Hangman!\n")
    start_options()


main()
