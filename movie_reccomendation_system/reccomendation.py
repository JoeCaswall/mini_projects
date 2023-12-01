"""An app which gives movie reccomendations based on
a user's previously watched films"""
from pathlib import Path
import json
from user_functions import *
from movie_functions import get_all_movies

class User():
    def __init__(self, name, movie_list):
        self.name = name
        self.movie_list = movie_list

    def all_genres(self):
        user_genres = get_user_genres("user_movies.json")
        genre_set = set(user_genres)
        print("The genres you've watched are:")
        for genre in genre_set:
            print(f"\t- {genre}")

my_data = get_user_data("user_movies.json")
solarwhale = User("Joe", my_data)


solarwhale.all_genres()