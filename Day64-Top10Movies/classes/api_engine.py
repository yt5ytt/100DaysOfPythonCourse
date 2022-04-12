import requests
import os

# *** This is class for TMDB API connection  *** #

API_KEY = os.environ.get("API_KEY")
ENDPOINT = "https://api.themoviedb.org/3/search/movie"


class MovieFinder:

    def __init__(self, title):
        response = requests.get(f"{ENDPOINT}?api_key={API_KEY}&query={title}")
        self.data = response.json()['results']
