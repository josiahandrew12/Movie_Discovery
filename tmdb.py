"""
Provides API calling function for TMDB
"""
import os
import random
import requests
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

IMG = "http://image.tmdb.org/t/p/w1280"
tmdb_api_key = os.getenv("tmdb_api_key")

params = {
    "api_key": tmdb_api_key
}

def movie_search1():
    """
Provides API calling  for movie 1
    """
    base_url_movie1 = "https://api.themoviedb.org/3/movie/37724"
    response_movie1 = requests.get(
        base_url_movie1,
        params=params,
    )

    response_json_movie_1 = response_movie1.json()
    genre_movie1 = response_json_movie_1["genres"]
    movie_genre = ""

    try:
        for genres in genre_movie1:
            genres_names = genres["name"]
            genres_names = " ".join((genres_names, movie_genre))

        file_path = response_json_movie_1["poster_path"]
        file_path = IMG + file_path

        return (file_path, response_json_movie_1["original_title"],
        response_json_movie_1["tagline"], genres_names)

    except KeyError:
        return"Couldn't fetch movie info!"

def movie_search2():
    """
    Provides API calling  for movie 2
    """
    base_url_movie2 = "https://api.themoviedb.org/3/movie/70160"
    response_movie2 = requests.get(
        base_url_movie2,
        params=params,
    )
    response_json_movie_2 = response_movie2.json()
    genre_movie2 = response_json_movie_2["genres"]
    movie_genre = ""
    try:
        for genres in genre_movie2:
            genres_names = genres["name"]
            genres_names = " ".join((genres_names, movie_genre))

        file_path = response_json_movie_2["poster_path"]
        file_path = IMG + file_path
        return (file_path, response_json_movie_2["original_title"],
         response_json_movie_2["tagline"], genres_names)

    except KeyError:
        return"Couldn't fetch movie info!"

def movie_search3():
    """
    Provides API calling  for movie 3
    """
    base_url_movie3 = "https://api.themoviedb.org/3/movie/49538"
    response_movie3 = requests.get(
        base_url_movie3,
        params=params,
    )

    response_json_movie_3 = response_movie3.json()
    genre_movie3 = response_json_movie_3["genres"]
    movie_genre = ""

    try:
        for genres in genre_movie3:
            genres_names = genres["name"]
            genres_names = " ".join((genres_names, movie_genre))

        file_path = response_json_movie_3["poster_path"]
        file_path = IMG + file_path
        return (file_path, response_json_movie_3["original_title"],
        response_json_movie_3["tagline"], genres_names)

    except KeyError:
        return"Couldn't fetch movie info!"

def movie_search4():
    """
    Provides API calling  for random movie 4
    """
    base_url_movie_random = "https://api.themoviedb.org/3/movie/"
    random_movie = random.choice(range(10000, 40000))
    new_url = base_url_movie_random + str(random_movie)

    response_movie_random = requests.get(
        new_url,
        params=params,
    )

    response_json_movie_random = response_movie_random.json()

    try:
        genre_movie_random = response_json_movie_random["genres"]
        movie_genre = ""
        for genres in genre_movie_random:
            genres_names = genres["name"]
            movie_genre = "".join(genres_names)
        movie_search4.title = response_json_movie_random["original_title"]
        file_path = response_json_movie_random["poster_path"]
        tagline = response_json_movie_random["tagline"]
        genre = movie_genre

        while movie_search4.title is None:
            movie_search4.title = "No Title"
        while file_path is None:
            file_path = "No Image with this movie"
        while tagline == "":
            tagline = "No taglines with this movie please refresh!"
        while genre == "":
            genre = "No genre with this movie please refresh!"
        file_path = IMG + file_path
        return (file_path,movie_search4.title,tagline,genre)
    except KeyError:
        return movie_search4()


movie_search1()
movie_search2()
movie_search3()
movie_search4()
