from pathlib import Path
import json

def get_user_data(data_path):
    path = Path(data_path)
    user_str = path.read_text()
    user_info = json.loads(user_str)
    return user_info

def get_user_genres(data_path):
    user_genres = []
    user_movies = get_user_data(data_path)
    for movie in user_movies:
        user_genres.append(user_movies[movie])
    return user_genres
