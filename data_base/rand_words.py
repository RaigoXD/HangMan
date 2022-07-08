"""
Module for generate a random word
"""
import local_data
import random

class Words:
    """
    Class for generate a random word using or local data
    or API for random words
    """

    def __init__(self, lang:str,source:str = "local") -> None:
        self.language = lang
        self.source = source

    def get_word(self, category:str) -> str:
        """
        return a random word with context gave by category
        """
        words = local_data.DATA[self.language][category]
        print(words)
        rand_index = random.randint(0,len(words)-1)
        word = words[rand_index]
        return word

