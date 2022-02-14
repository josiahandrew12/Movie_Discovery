"""
Provides API calling function for MediaWiki
"""
import requests
from tmdb import movie_search4

def wiki_link(title):
    """Grabs API info from Wikipedia"""
    wiki_url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "info",
        "inprop": "url"
    }

    wiki_movie = requests.get(
            wiki_url ,
            params=params,
        )
    response_wiki = wiki_movie.json()
    for data in response_wiki["query"]["pages"]:
        wiki_id = data
    final_link  = response_wiki["query"]["pages"][wiki_id]["fullurl"]

    return final_link
wiki_link(movie_search4.title)
