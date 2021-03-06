import random
from pip._vendor import requests

class WordGenenator:
    '''
    Gets a random word from https://random-word-api.herokuapp.com
    '''
    def generate_word(self):
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        str = response.content.decode("utf-8")
        str = str.replace('[', '')
        str = str.replace('"','')
        str = str.replace(']', '')
        return str