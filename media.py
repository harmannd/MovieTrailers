import webbrowser


class Movie():
    """ This class provides a way to store movie related information."""
    
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ Movie constructor.

        Args:
            movie_title (str): Title of movie.
            movie_storyline (str): Brief description of movie plot.
            poster_image (str): URL link to image of movie poster.
            trailer_youtube (str): URL link to movie trailer on youtube.
            
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens a browser window to the URL specificed."""        
        webbrowser.open(self.trailer_youtube_url)
