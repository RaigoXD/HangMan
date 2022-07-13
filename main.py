"""
    All configuration for the Hangman game
"""

import json
import os
from hang_man import hang_mang_start

FILE_PATH=os.path.dirname(__file__)

MAINMENU = """HangMan Game by Jhoan Raigoza
    -> Menu
    1 - Play
    2 - Config
    3 - show actual config
    4 - exit 
        """

CONFIGMENU = """Change configurations for HangMam Game
    1 - Change languages
    2 - Method for get the random words
    3 - Exit
        """
CATEGORIESLOCAL = """Select a category:
    1 - Animals
    2 - Feelings
    3 - Countries
    4 - Food 
"""

CATEGORIESAPI = """Select a category:
    1 - Animals
"""


def print_message(message : str):
    """
    print the message and wait for press any key
    """
    print(f"{message}\nPress Enter key to continue")
    input()


def get_option():
    """
    Get option from keyboard
    """
    option = int
    try:
        option = int(input())
        return option
    except ValueError:
        print_message("Please enter a number")
    return -1



def read_config_file() -> dict:
    """
    Read the config from file
    """
    try:
        with open(f"{FILE_PATH}/config.json", "r", encoding="utf-8") as file:
            data_config = json.load(file)
            file.close()
            return data_config
    except FileNotFoundError:
        print_message("Error:Something was wrong with the file config.json")


def build_config():
    """
    Build the initial configuration for the HangMan Game from config.json
    """
    try:
        initial_config = read_config_file()
        source = initial_config['source']
        language = initial_config['languages']
        print("All do it successfully in config") # borrar
        return source, language
    except KeyError:
        print_message("Error:Something was wrong with the file config.json")
        return "sp", "local" # Default if something was wrong


def save_config_to_file(new_lang: str, new_source: str):
    """
    Save a new config to file
    """
    try:
        new_config = read_config_file()
        new_config['source'] = new_source
        new_config['languages'] = new_lang
        with open(f"{FILE_PATH}/config.json", "w", encoding="utf-8") as file:
            json.dump(new_config,file)
            file.close()
    except KeyError:
        print_message("Error:Something was wrong with the file config.json")


def change_config(language : str, method_get_words : str):
    """
    show the options to change the configurations,
    and make a new ones for the game selected by user
    """
    new_lang = language
    new_source = method_get_words

    while True:
        os.system("clear") # clean the screen
        print(CONFIGMENU)
        option = get_option()
        if option == 1:
            os.system("clear") # Clean the screen
            print("Please select the language:\n\t1 - Spanish\n\t2 - English\n->", end="")
            option = get_option()
            if option == 1:
                new_lang = "sp"
            elif option == 2:
                new_lang = "en"
                new_source = "local"
            else:
                print_message("Please enter a valid option")
        elif option == 2:
            os.system("clear") # Clean the screen
            print("Please select the method for randoms words :\n\t1 - Local Data Base\n\t2 - API for random words\n->", end="")
            option = get_option()
            if option == 1:
                new_source = "local"
            elif option == 2:
                new_source = "api"
                new_lang = "sp"
            else:
                print_message("Please enter a valid option")
        elif option == 3:
            break
        else:
            print_message("Please enter a valid option")

    save_config_to_file(new_lang,new_source) # Save the news arguments
    return new_source,new_lang



def category_local():
    """
    Categories to play with the local data
    """
    category = str
    while True:
        os.system("clear") # Clean the screen
        print(CATEGORIESLOCAL)
        print("-> ",end="")
        option = get_option()
        if option == 1:
            category = "animales"
            break
        elif option == 2:
            category = "sentimientos"
            break
        elif option == 3:
            category = "paises"
            break
        elif option == 4:
            category = "comida"
            break
        else:
            print_message("Please enter a valid option")

    return category

def category_api():
    """
    Categories to play with the API for random words
    """
    category = str
    while True:
        os.system("clear") # Clean the screen
        print(CATEGORIESAPI)
        print("-> ",end="")
        option = get_option()
        if option == 1:
            category = "animales"
            break
        else:
            print_message("Please enter a valid option")

    return category


def game_config(lang: str, method_get_words:str):
    """
    config the game before start to play
    """
    category = str
    if method_get_words == "local":
        category = category_local()
    else:
        category = category_api()

    print_message(category) # Borrar
    hang_mang_start(lang, method_get_words, category)

def hang_man():
    """
    Main funtion for HangMan game
    """
    method_get_words,lang = build_config()

    print(f"lang: {lang}") # Borrar
    print(f"source {method_get_words}") #Borrar

    while True:
        os.system("clear") # clean the screen
        print(MAINMENU)
        option = get_option()
        if option == 1:
            game_config(lang,method_get_words)
        elif option == 2:
            method_get_words,lang = change_config(lang,method_get_words)
        elif option == 3:
            os.system("clear")
            print("Actual configuration is:")
            print(f"\tLanguages = {lang} \n\tSource of the randoms words: {method_get_words}")
            print_message("")
        elif option == 4:
            break
        else:
            print_message("Please enter a valid option")


if __name__ == '__main__':
    hang_man()
