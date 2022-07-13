"""
All features to play the hangman game
"""

from os import system  # just use system from this module
from randoms.rand_words import Words

HANGMAN_STATES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
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

    attempts = 0 # start
    while attempts < 6:

        system("clear")
        print(HANGMAN_STATES[attempts])
        temp_word_to_show = "".join(word_to_show)
        print(f"WORD: {temp_word_to_show}")
        print(word)

        character = str(input()[0])
        result = make_diff(word, character, word_to_show)

        if result is False:
            attempts += 1
        
        temp_word_to_show = "".join(word_to_show)
        if word == temp_word_to_show:
            print("You win")
            attempts = 6

        if attempts == 6:
            print("you lose")

    input()

def hang_mang_start(lang:str, source: str, category:str):
    """
    Function to init the game
    """
    generator = Words(lang, source) # Objet to generate the random words
    random_word = generator.get_word(category).lower() # random word return from data base

    word = remove_acents(random_word)  # the random word without acents
    word_to_show = ["-" for char in word]  # the temp word to show

    start_game(word, word_to_show)
