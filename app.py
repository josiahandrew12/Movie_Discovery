"""
Setting up our imports
"""
import os
import flask
from tmdb import movie_search1, movie_search2,movie_search3,movie_search4
from wiki import wiki_link

app = flask.Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    """Runs the flask App"""
    movie_searches1 = movie_search1()
    movie_searches2 = movie_search2()
    movie_searches3 = movie_search3()
    movie_searches4 = movie_search4()
    tmdb_wiki_link = movie_search4.title
    wiki_links = wiki_link(tmdb_wiki_link)

    return flask.render_template("index.html",
    movie_searches1=movie_searches1,num_movies1=len(movie_searches1),
    movie_searches2=movie_searches2,num_movies2=len(movie_searches2),
    movie_searches3=movie_searches3,num_movies3=len(movie_searches3),
    movie_searches4=movie_searches4,num_movies4=len(movie_searches4),
    wiki_links = wiki_links)

#We were shown to put this in our code because these are built in heroku variables allowing us to
#deploy our web app.But we got a pylint error.
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
