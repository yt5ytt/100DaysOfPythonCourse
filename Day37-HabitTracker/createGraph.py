import requests
import os

USERNAME = os.environ.get("USERNAME")
GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs"

class CreateGraph:

    def __init__(self, token):
        self.token = token
        self.headers = {
            "X-USER-TOKEN": self.token
        }
        self.params = {
            "id": "graph01",
            "name": "Running Graph",
            "unit": "Km",
            "type": "float",
            "color": "sora",
        }
        self.response = requests.post(url=GRAPH_ENDPOINT, json=self.params, headers=self.headers)
        print(self.response.text)