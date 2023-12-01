import pytest
from recommendation import User
from movie_functions import get_all_movies

@pytest.fixture
def tester_user():
    solarwhale = User("solarwhale", "user_movies.json")
    return solarwhale

@pytest.fixture
def all_movies():
    movies_list = get_all_movies("lots_of_movies.json")
    return movies_list

def test_user_genre(tester_user):
    assert tester_user.favourite_genre() == "Drama"

def test_user_recommendations_has_all_recs(tester_user):
    recs = tester_user.fav_recommendations()
    assert len(recs) == 4

def test_user_recs_correct(tester_user, all_movies):
    recs = tester_user.fav_recommendations()
    flag = True
    for movie in recs:
        print(movie)
        if movie not in all_movies:
            flag = False
    assert flag == True