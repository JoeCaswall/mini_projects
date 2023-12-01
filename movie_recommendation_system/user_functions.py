from pathlib import Path
import json

def get_user_data(data_path):
    try:
        path = Path(data_path)
        user_str = path.read_text()
        user_info = json.loads(user_str)
        return user_info
    except FileNotFoundError:
        print("No file at that location")

def get_user_genres(data_path):
    try:
        user_genres = []
        user_movies = get_user_data(data_path)
        for movie in user_movies:
            user_genres.append(user_movies[movie])
        return user_genres
    except FileNotFoundError:
        print("Sorry, no file found at that location")
