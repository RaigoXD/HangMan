"""
Module for generate a random word
"""
import random
import requests
import local_data

class Words:
    """
    Class for generate a random word using or local data
    or API for random words
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
        return a random word with context gave by category
        """
        if self.source == "local":
            return self.get_word_local(category)
        else:
            return self.get_word_api(category)


    def get_word_local(self, category) -> str:
        """
        return a random word with context by a category using the local data
        base
        """
        print("Take from local")
        words = local_data.DATA[self.language][category]
        print(f"palabras para animales {words}")
        rand_index = random.randint(0,len(words)-1)
        word = words[rand_index]
        return word


    def get_word_api(self, category) -> str:
        """
        return a random word with context gave by category using the
        api for random words
        """
        print("Take from api")
        word = str
        status_get = int
        if category == "animales":
            try:
                response = requests.get(url=self.url_animales)
                status_get = response.status_code
                body = response.json()['body']
                word = body['name']
                print(body)
            except:
                print(f"Error: Request fail {status_get}")
        
        return word



sisa = Words("sp", "api")
print(sisa.get_word("animales"))
