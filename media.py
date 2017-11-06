import webbrowser

class Movie():
    """"This class provides a way to store movies related information"""
    VALID_RATING = ["G", "PG", "PG-13", "R"]
    def __init__(self,movie_title,movie_stroyline,movie_poster,trailer_youtube_url):
        self.title = movie_title
        self.stoyline = movie_stroyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

