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

# Capital cities word bank
words = ('dublin reykjavik cardiff edinburgh belfast london oslo stockholm '
         'helsinki berlin copenhagen amsterdam brussels paris '
         'luxembourg lisbon madrid rome bern vienna warsaw '
         'prague bratislava vilnius riga tallinn bucharest budapest '
         'zagreb sarajevo ljubljana belgrade skopje sofia pristina '
         'minsk kiev tbilisi athens ankara vaduz podgorica valetta tirana '
         'nicosia chisinau moscow monaco tokyo seoul bejing kathmandu cairo '
         'canberra hanoi lima ottawa jerusalem santiago brasilia kingston '
         'havana wellington pyongyang taipei bangkok manila jakarta '
         'mogadishu ulaanbataar ').split()


def start_options():
    # print("   Press " + "» S  " + "to start new game")
    # print("   Press " + "» H  " + "for instructions")
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
    print("\n")
    print("A name of a city will be hidden behind blank spaces.\n"
    "You must find the correct letters by guessing every letter.\n"
    "Correct guesses will reveal a letter in the name.\nWrong guesses "
    "reduces a life. You have 7 lives.\n\nHope you have fun!")
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

def intro_title():
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


def main():
    intro_title()
    # print(hangman_intro_image[0])
    # print("   Welcome to Hangman!\n")
    start_options()


main()
