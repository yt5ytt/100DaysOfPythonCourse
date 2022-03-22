import requests

URL = "https://api.npoint.io/c790b4d5cab58020d391"

class FakePosts:

    def __init__(self):
        self.data = requests.get(URL).json()