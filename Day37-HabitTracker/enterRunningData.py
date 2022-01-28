import os
import requests

GRAPH_ID = os.environ.get("RUNNING_ID")
USERNAME = os.environ.get("USERNAME")
ENTER_RUNNING_DATA_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
# DAY = datetime.date.today()
DAY = "20220126"
HOW_MUCH = "5.0"


class EnterRunningData:

    def __init__(self, token):
        self.token = token
        self.headers = {
            "X-USER-TOKEN": self.token
        }
        self.params = {
            "date": DAY,
            "quantity": HOW_MUCH
        }
        self.response = requests.post(url=ENTER_RUNNING_DATA_ENDPOINT, headers=self.headers, json=self.params)
        print(self.response.text)
