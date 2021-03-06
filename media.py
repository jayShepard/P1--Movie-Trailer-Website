class Movie:
    """ This class provides a way to store movie related information"""

    def __init__(self, movie_title, poster_image, trailer_youtube, year,
                 director, writer, stars):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year
        self.director = director
        self.writer = writer
        self.stars = stars
