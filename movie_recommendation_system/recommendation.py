"""An app which gives movie reccomendations based on
a user's previously watched films"""
from pathlib import Path
from collections import Counter
import json
from user_functions import *
from movie_functions import get_all_movies

class User():
    """User class with attributes for their name and the 
    path to the file where their data is stored"""
    def __init__(self, name, movie_path):
        self.name = name
        self.movie_path = movie_path

    """methods to return a string of all the genres the user's watched,
    their most commonly watched genre, and some recommendations based on
    that genre"""
    def all_genres(self):
        user_genres = get_user_genres(self.movie_path)
        genre_set = set(user_genres)
        genres = "The genres you've watched are:"
        for genre in genre_set:
            genres += f"\n\t- {genre}"
        return genres
    
    def favourite_genre(self):
        user_genres = get_user_genres(self.movie_path)
        fav_genre = Counter(user_genres).most_common(1)
        # most_common returns a tuple inside an array
        print(f"Your favourite genre was {fav_genre[0][0]} with {fav_genre[0][1]} films")
        return fav_genre[0][0]

    def fav_recommendations(self):
        many_films = get_all_movies("lots_of_movies.json")
        user_genres = get_user_genres(self.movie_path)
        fav_genres = Counter(user_genres).most_common(1)
        fav_genre = fav_genres[0][0]
        recommendations_list = []
        for film in many_films:
            if many_films[film] == fav_genre:
                recommendations_list.append(film)
        recommendation = f"Some other {fav_genre}s you might enjoy:"
        for film in recommendations_list:
            recommendation += f"\n\t- {film}"
        print(recommendation)
        return recommendations_list


solarwhale = User("Joe", "user_movies.json")
genres = solarwhale.all_genres()


print(solarwhale.fav_recommendations())