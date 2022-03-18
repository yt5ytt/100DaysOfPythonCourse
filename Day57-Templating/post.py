import requests

POSTS_URL = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    
    def __init__(self):
        self.all_posts = requests.get(POSTS_URL).json()
    
    def get_post(self, id):
        for post in self.all_posts:
            if post["id"] == id:
                self.title = post["title"]
                self.subtitle = post["subtitle"]
                self.body = post["body"]