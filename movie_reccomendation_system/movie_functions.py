from pathlib import Path
import json

def get_all_movies(movie_path):
    path = Path(movie_path)
    contents = path.read_text()
    movies = json.loads(contents)
    return movies

