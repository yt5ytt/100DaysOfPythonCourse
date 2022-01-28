import requests

CREATE_ENDPOINT = "https://pixe.la/v1/users"


class CreateUser:

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.params = {
            "token": token,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        self.response = requests.post(url=CREATE_ENDPOINT, json=self.params)
        print(self.response.text)
