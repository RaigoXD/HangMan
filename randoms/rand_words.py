"""
Module for generate a random word
"""
import random
import json as js # using to read the local data base
import requests # using to read the random words from api


class Words:
    """
    Class to generate a random word using local data
    or API for random words

    lang: language used for random word

    source: from where the program gets the random words (Local, API)
    """
    language = str
    source = str

    #Urls API
    url_animales = "https://palabras-aleatorias-public-api.herokuapp.com/animal/random"

    def __init__(self, lang:str,source:str = "local") -> None:
        self.language = lang
        self.source = source


    def get_word(self, category:str) -> str:
        """
        return a random word with context gave by a category
        """
        if self.source == "local":
            return self.__get_word_local(category)
        else:
            return self.__get_word_api(category)


    def __get_word_local(self, category) -> str:
        """
        return a random word with context by a category using the local data
        base
        """
        word = str
        try:
            with open("local_data.json", "r", encoding="utf-8") as data_base:
                data = js.load(data_base)
                words = data[self.language][category]
                rand_index = random.randint(0,len(words)-1)
                word = words[rand_index]
        except (KeyError, ValueError,FileNotFoundError, IndexError):
            print("Error: Something was wrong in import the data base ")
        return word


    def __get_word_api(self, category) -> str:
        """
        return a random word with context gave by a category using the
        API for random words
        """
        print("Taking from api...")
        word = str
        status_get = int
        if category == "animales":
            try:
                response = requests.get(url=self.url_animales)
                status_get = response.status_code
                body = response.json()['body']
                word = body['name']
            except KeyError:
                print(f"Error: Request fail {status_get}")
        return word
