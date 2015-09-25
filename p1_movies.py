__author__ = 'yhu'
import fresh_tomatoes
'''How will I complete this project?
- Install Python
- Create a data structure (i.e. a Python Class) to store your favorite movies, including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.
- Create multiple instances of that Python Class to represent your favorite movies; group all the instances together in a list.
- To help you generate a website that displays these movies, we have provided a Python module called fresh_tomatoes.py - this module has a function called open_movies_page that takes in one argument, which is a list of movies and creates an HTML file which visualizes all of your favorite movies.
- Ensure your website renders correctly when you attempt to load it in a browser.
'''

#create a class with the following properties:
# movie title,
# box art URL (or poster URL)
# a YouTube link to the movie trailer.

class Movie(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url, release_date):
        self.title=title
        self.poster_image_url=poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date



movie1 = Movie("Terminator 2", "http://ia.media-imdb.com/images/M/MV5BMTg5NzUwMDU5NF5BMl5BanBnXkFtZTcwMjk2MDA4Mg@@._V1_SY317_CR18,0,214,317_AL_.jpg", "www.youtube.com/watch?v=eajuMYNYtuY", "1991")
movie2 = Movie("World War Z", "http://ia.media-imdb.com/images/M/MV5BMTg0NTgxMjIxOF5BMl5BanBnXkFtZTcwMDM0MDY1OQ@@._V1_SX214_AL_.jpg", "www.youtube.com/watch?v=HcwTxRuq-uk", "2013")
movie3 = Movie("Prometheus", "http://ia.media-imdb.com/images/M/MV5BMTY3NzIyNTA2NV5BMl5BanBnXkFtZTcwNzE2NjI4Nw@@._V1_SX214_AL_.jpg", "www.youtube.com/watch?v=sftuxbvGwiU", "2012")
movie4 = Movie("Secondhand Lions", "http://ia.media-imdb.com/images/M/MV5BMTIzNjcyOTcxNl5BMl5BanBnXkFtZTYwODE5Mjk2._V1_SX214_AL_.jpg", "www.youtube.com/watch?v=hzElnBgsr0s", "2003")
movie5 = Movie("Because of Winn-Dixie", "http://ia.media-imdb.com/images/M/MV5BMTA3NDYzNDE0MjBeQTJeQWpwZ15BbWU3MDc3NjA3MzM@._V1_SX214_AL_.jpg", "www.youtube.com/watch?v=hzElnBgsr0s", "2005")
movie6 = Movie("Salt", "http://ia.media-imdb.com/images/M/MV5BMjIyODA2NDg4NV5BMl5BanBnXkFtZTcwMjg4NDAwMw@@._V1_SX214_AL_.jpg", "www.youtube.com/watch?v=hzElnBgsr0s", "2010")
movie7 = Movie("Kick-Ass", "http://ia.media-imdb.com/images/M/MV5BMTMzNzEzMDYxM15BMl5BanBnXkFtZTcwMTc0NTMxMw@@._V1_SX214_AL_.jpg", "www.youtube.com/watch?v=rFpWpkxsVI8", "2002")
movie8 = Movie("The Dark Knight", "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg", "www.youtube.com/watch?v=EXeTwQWrcwY", "2012")
movie9 = Movie("The Dark Knight Rises", "http://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_SX214_AL_.jpg", "www.youtube.com/watch?v=g8evyE9TuYk", "2008")

movie_list = [movie1, movie2, movie3,movie4, movie5, movie6, movie7, movie8, movie9]


fresh_tomatoes.open_movies_page(movie_list)
