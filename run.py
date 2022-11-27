import random


def hangman_remaining_lives(lives):
    """
    Hangman images representing lives left
    """
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
        """,
        """
        |/
        |
        |
        |
        |
        |
        ========
        """,

        """
        |
        |
        |
        |
        |
        ========
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
        ||       /|\\    Press » 1  to start new game
        ||       / \\    Press » 2  for instructions
        ||              Press » 3  to select difficulty
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


def start_options():
    """
    Startup view, function to display user choice to either
    start game, view instructions or select difficulty
    (User choice is displayed in the hangman_intro_image)
    """
    print(hangman_intro_image[0])

    start = False

    while not start:
        choice = input("\n ")
        if choice == "1":
            start = True
            difficulty = "default"
            return difficulty

        elif choice == "2":
            start = True
            hangman_instructions()

        elif choice == "3":
            start = True

        else:
            print(f" You selected {choice}. "
                  "Please select 1, 2 or 3 to continue ♥")


def game_difficulty():
    """
    Function to select difficulty and return values to main.
    E for easy
    N for normal
    H for hard
    """
    print("\n")
    print("Please select a difficulty\n")
    print("Press E for Easy")
    print("Press N for Normal")
    print("Press H for Hard")

    difficulty = False

    while not difficulty:
        options = input("\n ").upper()
        if options == "E":
            difficulty = True
            difficulty_lives = 10
            return difficulty_lives

        elif options == "N":
            difficulty = True
            difficulty_lives = 7
            return difficulty_lives

        elif options == "H":
            difficulty = True
            difficulty_lives = 5
            return difficulty_lives

        else:
            print("\n Please choose E, N or H to select your difficulty")


def get_word():
    """
    Gets random word form cities.txt
    """
    word = random.choice(open("cities.txt", "r").read().split('\n'))
    return word.upper()


def play_game(word, difficulty_lives):
    """
    Starts the game and runs all gameplay logic
    """
    secret_word = "░" * len(word)
    game_over = False
    guesses = []
    lives = difficulty_lives
    print(f"\nRemaining Lives: {lives}\n")
    print("★  Your city to guess: " + " ".join(secret_word) + "\n")

    while not game_over and lives > 0:
        input_guess = input("Please guess a letter: \n").upper()
        try:
            if len(input_guess) > 1:
                raise ValueError(
                    f"\nYou can only guess one letter at the time. "
                    f"You guessed: {len(input_guess)}"
                )
            elif not input_guess.isalpha():
                raise ValueError(
                    f"\nOnly letters allowed."
                    f" You guessed: {input_guess}"
                )
            elif len(input_guess) == 1 and input_guess.isalpha():
                if input_guess in guesses:
                    raise ValueError(
                        f"\nYou have already guessed {input_guess}"
                        )
                elif input_guess not in word:
                    print(f"\nSorry, wrong guess... {input_guess}"
                          " is not in the word")
                    print("You lost a life. Better luck next time!")
                    guesses.append(input_guess)
                    lives -= 1
                else:
                    print(f"\nYou found a letter! {input_guess} is correct."
                          " GG!")
                    guesses.append(input_guess)
                    guessed_word_list = list(secret_word)
                    indices = [i for i, letter in enumerate(word)
                               if letter == input_guess]
                    for index in indices:
                        guessed_word_list[index] = input_guess
                        secret_word = "".join(guessed_word_list)
                    if "░" not in secret_word:
                        game_over = True
        except ValueError as input_error:
            print(f"{input_error}.\nPlease try again.\n")
            continue

        print(hangman_remaining_lives(lives))

        if lives > 0:
            print(f"\nRemaining Lives: {lives}\n")
            print("★  Your city to guess: " + " ".join(secret_word) + "\n")
            print("★  Your guesses: " + ", ".join(guesses) + "\n")

    if game_over:
        print(f"Congrats! You found the secret word: {word}")
    else:
        print("Oh shoot! You've run out of lives ✟")
        print("Game over.\n\n")
        print(f"The correct word was: {word}")

    restart_game(difficulty_lives)


def hangman_instructions():
    """
    Function to display game rules.
    Allows user to go back to main menu by pressing enter.
    """
    print("\n")
    print("A name of a city will be hidden behind blank spaces and\n"
          "you must find the correct city by guessing each letter.\n"
          "Correct guesses will reveal a letter in the name.\nWrong guesses "
          "will reduce a life.\n\nHope you have fun!\n")

    input("Press enter to return to main menu\n")
    print("\n")
    main()


def restart_game(difficulty_lives):
    """
    User can choose to start a new game immediately
    or return to main menu by pressing enter
    """
    reset_game = False
    while not reset_game:
        restart = input("Would you like to play another game? Y/N\n\n").upper()
        try:
            if restart == "Y":
                reset_game = True
                hangman_word = get_word()
                play_game(hangman_word, difficulty_lives)

            elif restart == "N":
                reset_game = True
                print("\n")
                main()

            else:
                raise ValueError(
                    f"You have to enter Y or N. You entered {restart}"
                )
        except ValueError as input_error:
            print(f"\n{input_error} is invalid. Please try again.\n")


def main():
    """
    Start the application and run the main functions
    """
    intro_title()
    difficulty = start_options()
    if difficulty == "default":
        difficulty_lives = 7
    else:
        difficulty_lives = game_difficulty()
    hangman_word = get_word()
    play_game(hangman_word, difficulty_lives)


main()
