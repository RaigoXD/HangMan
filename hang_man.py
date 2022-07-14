"""
All features to play the hangman game
"""

from os import system  # just use system from this module
from randoms.rand_words import Words

CLEANSCREEN = "clear"  # change it to "cls" if you are on windows

WINMESSAGE = """
               __,_,                ╦ ╦╔═╗╦ ╦  ╦ ╦╦╔╗╔
              [_|_/                 ╚╦╝║ ║║ ║  ║║║║║║║
               //                    ╩ ╚═╝╚═╝  ╚╩╝╩╝╚╝
             _//    __              
            (_|)   |@@|             FINALLY 
             \ \__ \--/ __          YOU SAVE THE WORD
              \o__|----|  |   __    
                  \ }{ /\ )_ / _/   GitHub: @RaigoXD
                  /\__/\ \__O (__   
                 (--/\--)    \__/   
                 _)(  )(_           
                `---''---`          YOU WON WITH THE WORD: """



LOSEMESSAGE = """
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|  ╦ ╦╔═╗╦ ╦  ╦  ╔═╗╔═╗╔═╗ 
      ,"                      ,"|        ,"        ,"  |  ╚╦╝║ ║║ ║  ║  ║ ║╚═╗║╣ 
     +-----------------------+  |      ,"        ,"    |   ╩ ╚═╝╚═╝  ╩═╝╚═╝╚═╝╚═╝
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |  GitHub: @RaigoXD
     |  |  PLEASE         |  |  |     |         |      |
     |  |  SAVE US!!      |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"     
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------  YOU LOSE THE WORD WAS: """


TITLEHANGMAN ="""
 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
                        by Jhoan Raigoza                                                                   
"""



HANGMAN_STATES = ['''
              +---+
              |   |
                  |  
                  |  
                  |    
                  |
            =========''','''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  | 
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========''']



def print_win_or_lose(win: bool, word : str):
    """
    print the win or lose message
    """
    system(CLEANSCREEN)
    if win is True:
        print(WINMESSAGE, end="")
    else:
        print(LOSEMESSAGE, end="")
    print(word.upper())
    print("--------------------------------------------------------------------------\n", end="")


def print_hangman(state : str, characters, word_to_show):
    """
    To print the title and state of the hangman
    """
    system(CLEANSCREEN)
    print(TITLEHANGMAN)
    print(f"Attempted characters :{characters}{state}\tWORD: {word_to_show}")
    print("--------------------------------------------------------------------------\n", end="")

def remove_acents(word : str):
    """
    Remove the acents from word
    """
    temp_word = word.maketrans('áéíóú', 'aeiou')
    return word.translate(temp_word)


def make_diff(word:str, character: str, word_to_show: list):
    """
    Change the word_to_show with the similarities between word and character
    """
    if character in word:
        for index,char in enumerate(word):
            if char == character:
                word_to_show[index] = character
            elif char == " ":
                word_to_show[index] = " "
        return True
    else:
        return False


def start_game(word : str, word_to_show : str):
    """
    Function to start to play the game
    """
    make_diff(word, " ", word_to_show) # Search if the word have spaces
    characters_try = []
    attempts = 0 # start
    game_win = bool
    while attempts < 6:

        temp_word_to_show = "".join(word_to_show)
        print_hangman(HANGMAN_STATES[attempts], characters_try,temp_word_to_show)

        character = str(input("")[0])
        result = make_diff(word, character, word_to_show)
        temp_word_to_show = "".join(word_to_show) # to show and compare with the original word
        characters_try.append(character)

        if result is False:
            attempts += 1

        if attempts == 6:
            game_win = False

        if word == temp_word_to_show:
            game_win = True
            break

    while True:
        print_win_or_lose(game_win, word)
        option = input("<Press Enter to play again or type (x) to exit the game or type (m) to back to main menu>")
        if option == "x":
            return "exit"
        elif option == "":
            return "play"
        elif option == "m":
            return "menu"
        else:
            print("Please selecte a valid option\nPRESS ENTER TO CONTINUE")
            input()


def hang_mang_start(lang:str, source: str, category:str):
    """
    Function to init the game
    """
    while True:
        generator = Words(lang, source) # Objet to generate the random words
        random_word = generator.get_word(category).lower() # random word return from data base

        word = remove_acents(random_word)  # the random word without acents
        word_to_show = ["-" for char in word]  # the temp word to show

        option = start_game(word, word_to_show)

        if option == "exit":
            return False
        elif option == "menu":
            return True
